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



class CallUserResource:
    def on_get(self, req, resp, id)
        """View user call status"""
        call_user = "{}"
        resp.body = json.dumps(call_user)

    def on_post(self, req, resp, action, id)
        """Activate and deactivate calls for user"""
        call_user = "{}"
        resp.body = json.dumps(call_user)



class CallResource:
    def on_get(self, req, resp)
        "View the status of scrum call"""
        call = "{}"
        resp.body = json.dumps(call)

    def on_post(self, req, resp, action)
        call = "{}"
        resp.body = json.dumps(call)


api = falcon.API()

# Add the routes
api.add_route('/users', UsersResource())
api.add_route('/user/{id}', UserResource())
api.add_route('/call/user/{id}/{action}', CallUserResource())
api.add_route('/call/{action}', CallResource())
