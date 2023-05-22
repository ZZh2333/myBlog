from . import route_musicGen
from flask import render_template, request
import numpy as np

@route_musicGen.route('/musicgen',methods=["Get","POST"])
def musicgen():
    return render_template('musicGen/musicgen.html')

@route_musicGen.route('/compose',methods=["Get","POST"])
def compose():
    return render_template('musicGen/compose.html')

@route_musicGen.route('/allmusic')
def allmusic():
    return render_template('musicGen/allmusic.html')

@route_musicGen.route('/musicplay')
def musicplay():
    return render_template('musicGen/musicplay.html')

@route_musicGen.route('/music',methods=["Get","POST"])
def music():
    # model = torch.load('.\motifModel.pth')
    # x1 = np.random.randint(50,70)
    # x2 = np.random.randint(25,40)
    # x3 = np.random.randint(50,80)
    # x4 = np.random.randint(15,40)
    # x5 = np.random.randint(80,130)
    # x = [131] + [x1,x2,x3,x4,x5] + [132] + [130] * 59
    # x = torch.LongTensor(x)
    # y = ''.join([" "+ str(i) for i in predict(x.unsqueeze(0))[0].tolist()])
    # midi_batch = []
    # for i,mus in enumerate(y.split(" ")):
    #     if(mus == str(132)):
    #         break
    #     if(mus != str(131) and mus != ""):
    #         midi_batch.append(mus)
    # midi_batch = midi_batch[1:]
    # print(midi_batch)
    # midi_array = []
    # for i in midi_batch:
    #     z = [0] * 130
    #     z[int(i)] = 1
    #     midi_array.append(z)
    # numpy_to_midi(torch.LongTensor(midi_array),'./pic9.mid')



    return render_template('musicGen/music.html')