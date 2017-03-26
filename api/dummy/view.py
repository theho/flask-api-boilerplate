from flask_classful import FlaskView, route


class DummyView(FlaskView):
    route_base = '/v1/dummy'

    def index(self):
        return 'I am such a dummy'

    def get(self, id):
        return '{} is such a dummy'.format(id)
