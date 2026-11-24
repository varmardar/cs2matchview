import json
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen

params = {'scope':'widget-matches','page[offset]':'0','page[limit]':'100','sort':'tier_rank,-start_date','filter[matches.status][in]':'current,upcoming','filter[matches.discipline_id][eq]':'1','with':'teams,tournament,ai_predictions,games,streams'}
url = 'https://api.bo3.gg/api/v1/matches?' + urlencode(params)
with urlopen(Request(url, headers={'Accept':'application/json','User-Agent':'CS2MajorOverlay/1.0'}), timeout=20) as response:
    data = json.load(response)
if not isinstance(data, (dict, list)):
    raise ValueError('Unexpected API response')
with open('matches.json','w',encoding='utf-8') as f:
    json.dump({'updated_at':datetime.now(timezone.utc).isoformat(),'payload':data}, f, ensure_ascii=False, separators=(',',':'))
