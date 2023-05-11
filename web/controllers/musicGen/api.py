from . import route_musicGen

@route_musicGen.route('/api')
def api():
    ans = 'zzh'
    return ans