# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

ALGORITHM_EXECUTIONS = {
    'execution1': {'algorithm': 'build an API'},
    'execution2': {'algorithm': '?????'},
    'execution3': {'algorithm': 'profit!'},
}


def abort_if_execution_doesnt_exist(execution_id):
    if execution_id not in ALGORITHM_EXECUTIONS:
        abort(404, message="Execution {} doesn't exist".format(execution_id))

parser = reqparse.RequestParser()
parser.add_argument('algorithm')


# Todo
# shows a single todo item and lets you delete a todo item
class Execution(Resource):
    def get(self, execution_id):
        abort_if_execution_doesnt_exist(execution_id)
        return ALGORITHM_EXECUTIONS[execution_id]

    def delete(self, execution_id):
        abort_if_execution_doesnt_exist(execution_id)
        del ALGORITHM_EXECUTIONS[execution_id]
        return '', 204

    def put(self, execution_id):
        args = parser.parse_args()
        execution = {'execution': args['execution']}
        ALGORITHM_EXECUTIONS[execution_id] = execution
        return execution, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class ExecutionList(Resource):
    def get(self):
        return ALGORITHM_EXECUTIONS

    def post(self):
        args = parser.parse_args()
        execution_id = int(max(ALGORITHM_EXECUTIONS.keys()).lstrip('execution')) + 1
        execution_id = 'execution%i' % execution_id
        ALGORITHM_EXECUTIONS[execution_id] = {'algorithm': args['algorithm']}
        return ALGORITHM_EXECUTIONS[execution_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(ExecutionList, '/executions')
api.add_resource(Execution, '/executions/<execution_id>')


if __name__ == '__main__':
    app.run(debug=True)
