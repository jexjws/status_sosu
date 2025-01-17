from flask import Blueprint, request, json, render_template
import yaml
 
web = Blueprint('web', __name__)

with open('./config.yml', 'r', encoding='utf-8') as f:
  config = yaml.load(f.read(), Loader=yaml.FullLoader)

@web.route('/', methods=['GET'])
def index():
  datas = []
  for client in config["client"].keys():
    with open(f'./sync/{client}.json', 'r', encoding='utf-8') as sf:
      data = json.loads(sf.read())
      data["clientname"] = client
      datas.append(data)
  return render_template('index.html', config=config["client"], datas=datas)