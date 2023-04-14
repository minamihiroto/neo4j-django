from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from neo4j import GraphDatabase
import json


# Neo4jデータベースに接続するためのドライバーを作成します。
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "your_password_here"))

def get_all_persons(request):
    # セッションを開始し、すべてのPersonノードを取得するクエリを実行します。
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p")

        # クエリ結果からすべてのレコードを取得します。
        records = list(result)

    # レコードを辞書のリストに変換します。
    persons = [{"name": record["p"]["name"], "age": record["p"]["age"]} for record in records]

    # JsonResponseを使用して、結果をJSON形式で返します。
    return JsonResponse({"persons": persons})

def create_person(request):
    if request.method == "POST":
        try:
            # POSTリクエストのJSONデータを読み込みます。
            data = json.loads(request.body)

            # 新しいPersonノードを作成するクエリを実行します。
            with driver.session() as session:
                session.run("CREATE (p:Person {name: $name, age: $age})", data)

            # 成功メッセージを返します。
            return JsonResponse({"message": "Person created successfully"})

        except Exception as e:
            # エラーが発生した場合は、BadRequestレスポンスを返します。
            return HttpResponseBadRequest(str(e))

    else:
        # POSTリクエスト以外の場合は、BadRequestレスポンスを返します。
        return HttpResponseBadRequest("Invalid request method")