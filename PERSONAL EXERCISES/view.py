from Flask import Blueprints
view = Blueprints( __name__,"view")
@view.route("/")
def home():
  return "my home page"