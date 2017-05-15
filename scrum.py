import falcon
import json


class UsersResource:
    def on_get(self, req, resp):
        """Get a list of users"""
        users = "{}"
        resp.body = json.dumps(users)


class UserResource:
    def on_get(self, req, resp, id):
        """Get details about a user"""
        user = "{}"
        resp.body = json.dumps(user)

    def on_post(self, req, resp, id):
        "Update user details"""
        user = "{}"
        resp.body = json.dumps(user)

    def on_put(self, req, resp):
        """Create a user"""
        user = "{}"
        resp.body = json.dumps(user)

api = falcon.API()

# Add the routes
api.add_route('/users', UsersResource())
api.add_route('/user/{id}', UserResource())
