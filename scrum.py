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
    def on_get(self, req, resp, id, call_id)
        """View user call status"""
        call_user = "{}"
        resp.body = json.dumps(call_user)

    def on_post(self, req, resp, id, call_id)
        """Activate and deactivate calls for user"""
        call_user = "{}"
        resp.body = json.dumps(call_user)



class CallResource:
    def on_get(self, req, resp, call_id)
        "View the details of scrum call"""
        call = "{}"
        resp.body = json.dumps(call)

    def on_post(self, req, resp, call_id)
        """Update the call details"""
        call = "{}"
        resp.body = json.dumps(call)

    def on_post(self, req, resp)
        """Add a new call"""
        call = "{}"
        resp.body = json.dumps(call)


class CallActionsResource:
    def on_post(self, req, resp, call_id, action):
        """Start or stop a call"""
        call_action = "{}"
        resp.body = json.dumps(call_action)


api = falcon.API()

# Add the routes
api.add_route('/users', UsersResource())
api.add_route('/user/{id}', UserResource())
api.add_route('/call/user/{id}/{call_id}', CallUserResource())
api.add_route('/call/manage/{call_id}/{action}' CallActionsResource())
api.add_route('/call/{call_id}/{action}', CallResource())
