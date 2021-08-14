import falcon
from demo import Management
app = falcon.API()
app.add_route('/management',Management())