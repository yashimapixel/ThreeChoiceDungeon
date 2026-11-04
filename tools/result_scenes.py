"""Scene specs for every result still (token language: see tools/scene_kit.py).
Key: "<event>:<choice index>:<branch r|ok|ng>". Bespoke drawings in gen_results.py take precedence."""
SCENES = {}


def add(text):
    for line in text.strip().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            k, v = line.split(' ', 1)
            SCENES[k] = v.strip()


# ------------------------------------------------------------ tier 1
add('''
e001:0:r  BG X:door_open@84,70 X:chest_open@84,90 X:coins@84,92,6 H:stand@40
e001:1:ok BG X:door_fallen@84,72 H:push@54 X:item@100,54,rope noicons
e001:1:ng B H:hurt@56 X:splat@68,54,3
e001:2:ok BG X:door_open@84,70 H:walk@84,78,26 FX:quiet
e001:2:ng B X:text@84,40,5 H:run@30f
e001:3:r  bg=corridor H:walk@84,96,24 FX:dark FX:wound1
e002:0:r  BG H:reach@46 X:flame@64,60,5 X:rats@130,92,6
e002:1:ok B H:run@84 X:blood@84,98,10
e002:1:ng BG X:rats@84,92,22 H:down@84,97
e002:2:ok BG H:stand@84 X:rats@150,90,3 FX:quiet
e002:2:ng B H:cower@84 FX:mad2
e002:3:r  BG X:rats@110,92,16 H:walk@40f
e003:0:ok B H:kneel@64f X:item@84,58,torch X:coins@64,92,5 noicons
e003:0:ng B H:cower@76f X:splat@30,62,2 FX:mad1
e003:1:r  B H:kneel@60f X:item@46,74,key noicons
e003:2:r  B H:pray@64f X:light@30,50,34
e004:2:r  B H:walk@140,94,32 X:text@84,58,2
e005:0:ok B X:light@84,62,44 H:stand@36 X:sparkle@84,40,6
e005:0:ng B X:eyes@84,60,5 H:stand@36 X:text@84,58,3
e005:1:ok B H:drink@40 X:cup@46,78 X:sparkle@40,56,4
e005:1:ng B H:hurt@40 X:blood@44,96,8 X:cup@60,92
e005:2:ok B H:listen@36 X:light@84,64,22
e005:2:ng B X:hand@78,44 X:hand@92,48 X:hand@86,40 H:run@140
e006:0:ok BG H:slash@40+sword X:goblin@84,98,12 X:coins@112,92,6 X:item@130,60,potion noicons
e006:0:ng BG X:goblin@80,92 X:goblin@104,92 X:goblin@128,92 H:run@34f
e006:1:ok B H:walk@124,94,30
e006:1:ng B H:hurt@120f X:splat@120,58,3
e006:2:ok B H:stand@104f X:stairs@140,98,4
e006:2:ng B H:cower@108f X:text@62,50,6
e007:0:r  B H:reach@40 X:blood@84,58,6 X:sparkle@84,40,4
e007:1:ok B H:pray@40 X:light@40,0,60
e007:1:ng B H:pray@40 X:eyes@84,30,6
e007:2:ok B H:run@134 X:coins@140,74,3
e007:2:ng B H:hurt@124f X:cracks@124,60,3
e008:2:ok BG H:walk@84 X:girl@150,92,12 FX:quiet
e008:3:r  BG X:girl@140,92,20 H:run@60f
e009:0:ok B H:sleep@44,96
e009:0:ng B H:sit@44 X:eyes@84,40,8 X:hands@130,99,3
e009:1:r  B H:sit@44
e009:2:r  B H:reach@46 X:flame@62,60,4
e009:3:r  B H:sit@44+sword
e010:0:r  B H:reach@40 X:blood@44,96,6
e010:1:r  B H:reach@40 FX:mad1 X:text@50,40,3
e010:2:r  B H:reach@40 FX:doom1
e010:3:r  BG H:walk@84 FX:dark
e011:0:r  B X:tightrope@84,62,60 H:walk@84,62,26
e011:1:ok B H:jump@84,62,32
e011:1:ng B H:climb@84,86,30 X:blood@84,92,8
e011:2:ok bg=cave H:fall@84,58 X:sparkle@84,86,6 X:hole@84,96,20
e011:2:ng bg=black H:fall@84,52 X:splat@84,84,8 X:hole@84,96,24
e012:0:r  BG X:fire@84,96,8 X:coins@84,94,6 H:stand@30+lantern
e012:1:ok BG H:slash@60+sword X:web@124,30,36
e012:1:ng BG X:spider@84,36 X:rope@84,0,30 H:hurt@84 FX:mad1
e012:2:ok BG H:kneel@60 X:figure@104,94,30
e012:2:ng BG X:spiderlings@84,90,40 H:cower@84
e013:0:ok B H:back@84,98,34 X:sparkle@84,40,4
e013:0:ng B H:back@84,98,34 X:mouth@84,38,9
e013:1:r  BG H:slash@60 X:cracks@110,40,4 X:blood@70,96,6
e013:2:r  B H:walk@84,98,30 X:eyes@84,40,6
e014:0:ok BG X:slime@84,98,10 H:slash@50+sword X:coins@92,94,6
e014:0:ng B H:hurt@38+sword X:splat@46,64,3
e014:1:r  BG H:reach@50 X:flame@68,60,5 X:slime@136,98,8
e014:2:ok B H:walk@146,94,30
e014:2:ng B H:hurt@140f X:blood@140,96,6
e015:0:ok B H:kneel@50 X:light@60,40,30
e015:0:ng B H:kneel@50 FX:doom1 X:text@84,40,3
e015:1:r  B H:pray@50 X:light@84,20,50
e015:2:ok B H:reach@50 X:item@70,70,holy noicons
e015:2:ng B H:stand@50 FX:quiet
e015:3:r  BG H:walk@40f X:text@100,50,5
e016:0:ok B H:jump@84,68,30
e016:0:ng B H:fall@84,70,30 X:splat@84,90,4
e016:1:r  bg=stairs H:walk@84,88,26 X:sparkle@84,30,6
e016:2:r  bg=corridor H:walk@84,96,24 FX:dark FX:wound1
e017:0:ok BG X:figure@40,94,34 H:stand@100f X:item@70,70,key noicons
e017:0:ng BG P:face@84 X:bones@40,92,6 H:stand@64
e017:1:ok B H:listen@80f X:sparkle@40,40,4
e017:1:ng B H:cower@84f X:text@40,40,8 FX:mad2
e017:2:r  B H:walk@130 X:text@50,48,3
e018:0:ok B H:drink@40 X:sparkle@40,50,4
e018:0:ng B H:sit@40 FX:mad3
e018:1:ok B H:kneel@40 X:item@60,70,potion noicons
e018:1:ng B H:hurt@40 X:sparkle@40,46,6
e018:2:r  B H:walk@150,94,28
e019:1:ok BG X:figure@120,94,30 H:push@50
e019:1:ng B H:hurt@40
e019:2:r  B H:walk@150,94,28 FX:doom1
e020:1:ng BG H:hurt@60 X:blood@60,96,5 X:dog@140,88
e020:2:r  BG X:dog@150,86 H:stand@50 FX:quiet
e021:0:r  B H:stand@40 X:book@84,62
e021:1:r  B H:carry@40 X:book@54,70
e021:2:r  BG X:fire@84,96,4 X:book@84,84 H:stand@40 X:text@100,40,3
e022:0:ok B H:kneel@60
e022:0:ng B H:hurt@60
e022:1:ok B H:swim@84,82,34 X:coins@112,90,4
e022:1:ng B H:swim@84,82,34 X:hand@84,74
e022:2:r  B H:kneel@60 X:sparkle@60,50,3
e023:1:ok BG X:knight@114,94,46 H:slash@50+sword
e023:1:ng BG X:knight@114,94,46 H:down@50
e023:2:r  B H:walk@140,94,30
e024:0:ok B H:cower@84
e024:0:ng B H:cower@84 FX:mad2
e024:1:ok B H:run@84
e024:1:ng B H:hurt@84 X:splat@84,60,10
e024:2:r  BG X:dog@100,86 X:bats@84,10,6 H:stand@60
e024:3:ok BG H:kneel@84 X:coins@104,92,6 X:bats@84,10,3
e024:3:ng B H:hurt@84 X:splat@84,56,6
e025:0:ok B H:stand@40 X:sparkle@98,40,6
e025:0:ng B H:stand@40 FX:doom2
e025:1:ok B H:point@40 X:coins@62,92,8
e025:1:ng B H:hurt@40 FX:mad1
e025:2:r  BG X:bones@90,92,12 X:coins@108,94,6 H:push@50
e026:0:ok BG X:door_open@84,70 X:stairs@84,98,5 H:walk@84,92,26
e026:0:ng BG X:door_open@84,70 X:bones@84,74,16 H:cower@44 FX:mad3
e026:1:ok B H:listen@60 X:item@84,80,map noicons
e026:1:ng B H:cower@50 X:splat@84,50,6
e026:2:r  B H:walk@140,94,30
e027:0:ok B H:stand@40 X:light@84,40,40
e027:0:ng B H:cower@40 X:eyes@84,60,4
e027:1:ok B H:reach@50 X:coins@84,88,6
e027:1:ng B H:hurt@50 X:hand@72,64
e027:2:r  B X:girl@112,92,22 H:stand@40
e027:3:r  B H:walk@140,94,30 X:text@84,40,3
e028:0:r  B H:reach@40 X:blood@60,96,6
e028:1:r  B H:kneel@40 FX:mad2 FX:heal1
e028:2:ok B H:kneel@44 X:item@84,88,amulet noicons
e028:2:ng B H:hurt@44 X:cracks@60,60,3
e029:0:ok BG X:figure@122,98,18 H:fight@60+sword X:coins@124,92,8
e029:0:ng B H:hurt@50 X:blood@50,96,8
e029:1:ok BG H:point@60 X:figure@144,94,28
e029:1:ng B H:down@50
e029:2:r  BG X:dog@100,86 H:stand@50 X:coins@124,94,4
e029:3:r  B H:arms_up@50
e030:0:ok B H:stand@40 X:sparkle@84,50,6
e030:0:ng B H:cower@40 FX:mad3
e030:1:r  BG H:slash@60 X:cracks@100,56,4
e030:2:ok BG H:carry@60 X:sparkle@84,40,4
e030:2:ng BG H:hurt@60 X:splat@70,60,5
e031:0:ok B H:stand@40 X:light@84,30,50
e031:0:ng B H:cower@40 X:eyes@84,50,8
e031:1:ok B H:reach@40 X:sparkle@84,40,3
e031:1:ng B H:hurt@40 FX:mad1
e031:2:r  B H:walk@140,94,30
e032:0:ng B H:push@60
e032:1:ng B H:hurt@60 X:cracks@84,60,4
e032:2:r  B H:kneel@44 X:coins@44,92,4
''')

# ------------------------------------------------------------ tier 2
add('''
g025:2:ok B H:climb@84,44,30 X:hands@84,99,5
g025:2:ng B X:hands@84,99,8 H:down@84,97 X:blood@84,98,14
g025:3:ok BG X:bones@84,94,20 H:walk@84,90,32 X:light@84,30,40
g025:3:ng B H:cower@84 X:text@84,40,8 FX:mad3
g025:4:r  BG X:bones@84,94,16 H:walk@84,90,30 FX:doom3
e033:0:ok B H:kneel@84 X:coins@104,92,10
e033:0:ng BG X:bones@84,86,40 H:down@84,97 X:hand@64,76
e033:1:r  B H:pray@84 X:light@84,10,50
e033:2:ok B H:run@84
e033:2:ng B H:down@84,97 X:bones@84,92,14
e034:0:r  BG X:light@84,30,50 X:sparkle@84,40,14 H:reach@50 X:coins@84,90,4
e034:1:ok BG X:bones@100,92,8 X:ghost@108,60,16 H:kneel@60 FX:quiet
e034:1:ng BG X:ghost@84,56,28 H:hurt@84 FX:mad1
e034:2:ok BG X:ghost@84,58,22 H:stand@84,94,38 FX:quiet
e034:2:ng BG X:ghost@84,56,26 H:cower@84 FX:mad2
e035:0:ok BG P:coffin@24 X:figure@104,96,8 H:reach@50 X:item@104,62,amulet X:coins@104,92,6 noicons
e035:0:ng B X:hand@100,40 H:hurt@120f
e035:1:ok B H:fight@44 FX:quiet
e035:1:ng B H:hurt@44 X:splat@50,52,4
e035:2:ok B H:listen@50 X:stairs@140,98,4
e035:2:ng B H:cower@44 X:text@84,40,6 FX:mad3
e036:0:ok B H:swim@84,66,30
e036:0:ng B H:swim@84,66,30 X:tentacles@84,99,3
e036:1:r  B X:tightrope@84,40,80 H:climb@84,52,28
e036:2:ok BG H:stand@84,94,34 FX:quiet
e036:2:ng B H:sit@84,60,26 FX:mad2 FX:dark
e037:0:r  B X:coins@64,64,6 X:stairs@140,96,3
e037:1:r  B H:sit@70,68,22 FX:mad2
e037:2:ok BG X:water@84,66 P:boatman@0,0 H:stand@84,68,28 X:hand@40,60 FX:doom2
e037:2:ng BG X:water@84,66 H:swim@84,80,30 X:hooded@100,66,34
e037:3:r  BG X:water@84,66 H:walk@40,66,24 FX:dark
e038:0:ok BG H:slash@50+sword X:skull@110,92 X:blood@110,96,14
e038:0:ng B H:hurt@40+sword X:splat@46,60,6
e038:1:r  BG H:fight@60+sword X:light@70,40,30 P:ghoul@60,0
e038:2:ok B H:walk@20f FX:quiet
e038:2:ng B H:down@40,97 X:splat@40,80,8
e039:1:r  B H:reach@110f X:item@100,60,potion noicons
e039:2:ok BG X:blood@96,94,14 X:hooded@50,94,40 H:run@140
e039:2:ng BG X:hooded@50,94,40 H:hurt@130f X:cracks@130,60,4
e040:0:ok B H:sit@40 X:coins@84,64,4
e040:0:ng B H:sit@40 X:eyes@84,40,8 FX:mad3
e040:1:ok BG H:fight@50 X:sparkle@90,70,10 X:bones@90,90,4
e040:1:ng BG H:hurt@50 X:splat@90,70,8
e040:2:r  B H:walk@140,94,30 X:text@84,40,2
e041:0:ok B H:reach@84,98,30 X:light@84,30,24
e041:0:ng B H:hurt@84,98,30 X:cracks@84,40,3
e041:1:r  BG H:slash@50+sword X:cracks@100,40,4 X:text@110,30,4
e041:2:ok BG H:carry@70 X:coins@84,90,6
e041:2:ng BG H:hurt@70
e042:0:ok B H:walk@84,52,22
e042:0:ng B H:cower@84,52,22 X:hands@84,99,6
e042:1:ok B H:run@118,50,24
e042:1:ng B H:climb@84,62,22 X:hands@84,99,3
e042:2:r  B X:rope@84,0,40 H:walk@84,52,22
e042:3:ok bg=chasm H:fall@84,50,30 X:water@84,86
e042:3:ng bg=chasm H:fall@84,56,30 X:splat@84,90,8
e043:0:ok B H:drink@40 X:flame@40,58,6
e043:0:ng B H:hurt@40 X:flame@48,60,4
e043:1:ok B H:drink@40 X:light@40,50,30
e043:1:ng B H:cower@40 X:light@40,40,70 FX:mad1
e043:2:ok B H:drink@40 X:rays@40,10,7
e043:2:ng B H:hurt@40 X:cracks@40,60,4
e044:0:ok B H:sit@84,70,24 X:light@84,40,40
e044:0:ng B H:hurt@84 FX:mad4
e044:1:ok B H:drink@84,90,30 X:coins@120,60,6
e044:1:ng B H:cower@84 X:blood@84,98,20
e044:2:r  B H:walk@150,94,26
e045:1:ok BG X:knight@100,94,40 H:kneel@60 X:item@80,60,sword noicons
e045:1:ng BG H:pray@60 X:bones@100,92,4 X:skull@108,88 FX:dark
e046:1:ok B H:kneel@84 X:book@84,92 X:girl@120,92,16
e046:1:ng BG X:girl@84,70,40 H:cower@40 FX:red
e046:2:r  B H:stand@60 X:light@100,60,20
e047:0:ok B H:stand@50 X:rays@50,40,6
e047:0:ng B H:hurt@50 X:splat@50,56,6
e047:1:r  BG X:figure@120,94,34 H:stand@50 X:stairs@150,98,3
e047:2:r  B H:walk@150,94,26 X:text@84,40,4
e048:0:ok B H:reach@50 X:item@74,60,key noicons
e048:0:ng B H:cower@40
e048:1:ok BG X:bones@100,92,10 X:coins@100,94,8 H:fight@50+sword X:item@100,70,key noicons
e048:1:ng B H:down@40,97
e048:2:ok B H:sit@30 FX:quiet
e048:2:ng BG P:cage@0,10 H:sit@84,80,24 FX:dark
e049:0:ok B H:walk@84,90,26
e049:0:ng B H:cower@84 X:text@84,40,6
e049:1:r  B H:reach@84 X:flame@100,62,4
e049:2:ok BG X:door_open@84,70 H:walk@84,90,26 FX:dark
e049:2:ng bg=black X:eyes@84,50,14 H:cower@84 X:hands@84,99,6
e049:3:r  B H:walk@84,90,26 FX:mad1
e050:1:r  B H:stand@120f X:stairs@140,98,4
e050:2:ok B H:run@140
e050:2:ng B H:down@140,97 X:cracks@140,70,3
e051:0:ok B H:carry@110f X:item@84,40,map noicons
e051:0:ng B H:hurt@84 X:hand@60,58
e051:1:ok BG X:bones@50,92,8 H:stand@100f X:stairs@140,98,3
e051:1:ng B H:sit@84,70,24 X:text@84,40,10 FX:mad2
e051:2:r  B H:kneel@70 X:coins@70,92,4
e052:0:ok B H:carry@84 X:book@92,70 X:rays@84,10,7
e052:0:ng B H:cower@84 X:text@84,50,14 FX:mad4
e052:1:r  B X:fire@84,96,6 H:stand@40 X:coins@84,92,4
e052:2:ok B H:carry@84 X:book@92,70 FX:heal1
e052:2:ng B H:cower@84 X:book@100,90 FX:mad2
e053:0:ok B H:run@30f
e053:0:ng BG X:water@84,64 H:swim@40,80,30 X:text@120,40,4
e053:1:ok B H:stand@30 X:coins@50,92,6 X:sparkle@84,40,4
e053:1:ng B H:cower@30 FX:mad3
e053:2:ok BG X:water@84,40 X:monster@120,86,30 H:swim@60,60,30 X:stairs@40,98,3
e053:2:ng BG X:water@84,50 X:hands@84,99,9 H:swim@84,62,30
e054:0:ok B H:stand@24 X:light@40,40,40
e054:0:ng B H:hurt@24 X:blood@30,96,8
e054:1:ok B H:sit@24 X:sparkle@62,60,6
e054:1:ng B H:sit@24 FX:mad4
e054:2:ok BG H:run@40f X:hooded@120,94,46
e054:2:ng BG H:hurt@40f X:hooded@120,94,46 X:splat@50,56,6
e055:0:ok B H:walk@84,90,32
e055:0:ng B H:down@84,92 FX:mad2
e055:1:r  B X:fire@84,96,8 H:stand@20 X:coins@84,90,6
e055:2:ok B H:run@84
e055:2:ng B H:cower@84 X:spiderlings@84,80,20 FX:mad2
e056:0:r  B H:stand@40 X:book@84,62 X:girl@140,92,14
e056:1:r  B H:carry@40 X:light@40,50,20
e056:2:r  B H:walk@150,94,26 X:text@84,50,3
e057:0:r  BG X:door_open@84,72 H:walk@84,90,26
e057:1:ok BG X:door_open@84,72 H:walk@84,90,26 FX:quiet
e057:1:ng B H:hurt@50 X:blood@60,96,10
e057:2:ok B H:push@64
e057:2:ng B H:hurt@84 X:splat@84,56,10
e057:3:r  bg=corridor H:walk@84,96,22 FX:dark FX:mad1
''')

# ------------------------------------------------------------ tier 3
add('''
g050:2:ok B H:run@84,99,22
g050:2:ng BG P:golem@-40 H:fall@130,50,30 X:splat@120,60,6
g050:3:ok BG X:bones@84,92,6 P:golem@0,20 H:fight@40+sword
g050:3:ng B H:down@30,98 X:blood@40,98,14
g050:4:ok B H:pray@84,99,22 X:light@84,40,30
g050:4:ng B X:rays@84,22,7 H:hurt@84,99,26 X:flame@84,96,6
e058:0:ok B H:walk@84,94,32 X:sparkle@84,50,10
e058:0:ng B H:hurt@84 X:sparkle@84,64,20 FX:mad1
e058:1:ok BG X:coins@104,92,10 X:figure@60,94,12 X:figure@72,94,10 H:stand@40 X:light@84,60,30
e058:1:ng B X:hands@84,99,6 H:cower@84 FX:mad3
e058:2:r  bg=fungus X:fire@84,96,12 H:run@84
e059:0:ok BG H:kneel@84 X:coins@104,92,12 X:flame@120,92,4
e059:0:ng BG X:figure@60,94,30 X:figure@108,94,26 X:cup@84,80 H:sit@84,94,30 FX:mad3
e059:1:ok B H:walk@84,94,26 X:light@84,40,40
e059:1:ng B X:eyes@84,40,14 H:cower@84
e059:2:ok BG X:stairs@120,98,5 H:walk@84,94,30
e059:2:ng BG X:monster@140,96,40 H:run@60f
e060:0:ng B H:hurt@120f X:hand@100,56 FX:mad2
e060:1:ng B H:kneel@124f FX:mad2
e060:2:r  BG H:kneel@100f X:coins@84,92,6 X:chest_open@60,90
e061:0:r  B H:reach@30 X:flame@46,60,5 X:sparkle@84,40,16
e061:1:r  B H:arms_up@30 X:rays@84,10,9 X:light@30,60,20
e061:2:ok BG H:slash@60+sword X:monster@120,96,20 X:text@84,30,8 X:light@84,10,40
e061:2:ng B H:cower@30 X:sparkle@50,60,24 FX:mad3
e062:0:ok B H:run@30f
e062:0:ng B H:hurt@30 X:tentacles@40,99,2
e062:1:r  BG X:fire@84,96,4 X:flame@84,80,16 H:stand@30+lantern
e062:2:ok BG X:bones@84,92,6 X:sparkle@84,80,10 H:fight@50
e062:2:ng BG H:hurt@60 X:sparkle@70,60,20 X:figure@110,94,40
e063:0:ok B H:walk@84,94,26 X:light@84,70,30
e063:0:ng B H:fall@84,40,26 X:rays@84,0,7
e063:1:ok BG X:coins@84,94,14 X:sparkle@84,40,10 H:carry@40
e063:1:ng B H:hurt@50 X:blood@50,96,6
e063:2:ok B X:stairs@84,98,5 H:walk@84,90,24
e063:2:ng B H:stand@84 FX:mad3
e064:0:ok B H:pray@84 X:light@84,60,30 X:rays@84,40,5
e064:0:ng B H:pray@84 X:text@84,30,8 FX:mad3
e064:1:ok B H:reach@50 X:sparkle@84,40,10
e064:1:ng B H:hurt@50 X:cracks@60,60,4
e064:2:r  B H:reach@50 X:light@84,40,50 X:sparkle@84,40,14
e065:0:ok BG X:door_open@70,70 X:stairs@70,98,4 H:walk@70,94,26
e065:0:ng B H:stand@70,94,26 X:text@98,40,6
e065:1:ok BG X:door_open@98,70 X:stairs@98,98,4 H:walk@98,94,26
e065:1:ng B X:hands@98,60,4 H:hurt@84
e065:2:ok BG X:door_open@84,70 H:point@50 X:girl@120,92,16 X:girl@140,92,16
e065:2:ng B H:cower@84 X:text@84,40,10 FX:mad2
e066:0:ok B H:carry@84 X:coins@84,90,24 X:sparkle@84,60,14
e066:0:ng B H:hurt@84 X:flame@84,94,10 X:fire@84,99,6
e066:1:ok B H:reach@30 X:item@50,60,amulet noicons
e066:1:ng B H:hurt@30
e066:2:r  B H:pray@84,99,30 X:light@20,40,30
e067:0:ok B H:fight@40+sword X:light@40,40,30
e067:0:ng B H:down@40,98 X:shadow@100,94,40
e067:1:ok BG H:arms_up@84 X:light@84,40,40
e067:1:ng BG H:cower@84 X:shadow@110,94,46 FX:mad2
e067:2:r  BG H:fight@60+lantern X:light@60,60,40 X:sparkle@110,80,4
e068:0:r  B H:reach@40 X:item@60,60,potion noicons
e068:1:r  B H:hurt@40 X:cracks@40,56,2 FX:heal2
e068:2:ok BG X:bones@84,92,6 X:item@70,70,potion X:item@100,70,holy X:coins@84,94,8 H:stand@40 noicons
e068:2:ng B H:hurt@40 X:sparkle@40,56,4 FX:doom2
e069:0:ok BG X:blood@84,96,24 X:cracks@84,70,3 H:fight@40
e069:0:ng B H:hurt@40 X:tentacles@84,90,2
e069:2:r  B H:walk@150,94,26 X:cracks@84,50,3
e070:0:ok B H:walk@84,94,26 X:stairs@150,98,3
e070:0:ng B H:cower@84 X:blood@84,98,12
e070:1:r  BG X:knight@40,94,40 X:knight@128,94,40 H:walk@84,94,30 X:light@84,40,40
e070:2:ok B H:cower@156,98,22 FX:quiet
e070:2:ng B H:hurt@156f
e071:0:r  B H:hurt@120f X:sparkle@120,50,6
e071:1:r  B H:reach@120f X:item@100,60,potion noicons
e071:2:ok B H:listen@120f X:stairs@150,98,3
e071:2:ng B H:cower@120f X:text@90,50,6 FX:mad2
e072:0:r  bg=ruins H:stand@40 X:book@84,80 X:light@84,60,20
e072:1:r  bg=ruins H:carry@84 X:book@92,70 X:light@84,50,30
e072:2:r  bg=ruins H:stand@40 X:text@100,40,10 X:book@100,90 FX:mad2
e073:0:ok B H:reach@40 X:item@60,60,map noicons
e073:0:ng BG X:figure@30,94,36 X:figure@60,94,32 X:figure@108,94,32 X:figure@140,94,36 H:cower@84
e073:1:ok BG H:carry@60 X:book@70,72 X:coins@84,94,6
e073:1:ng BG X:bones@84,90,14 H:down@84,97 X:book@60,90
e073:2:ok BG H:walk@84,94,26 FX:quiet
e073:2:ng B H:hurt@140f X:text@84,40,6
e074:0:ok B H:drink@40 X:light@40,50,30
e074:0:ng B H:drink@40 FX:mad2
e074:1:r  B H:kneel@44 X:blood@60,96,8
e074:2:r  B H:drink@40 X:light@84,40,50 X:sparkle@84,60,10
e075:0:ok BG X:figure@110,94,30 X:figure@136,94,30 H:stand@60 X:item@84,70,potion X:coins@84,94,6 noicons
e075:0:ng B H:hurt@84,80,30 X:rope@84,0,50
e075:1:ok B H:pray@84 X:light@84,10,40
e075:1:ng B H:pray@84 X:text@100,30,6 FX:mad3
e075:2:r  B H:walk@150,94,26 X:text@84,40,4
e076:0:ok B H:kneel@84,60,24 X:light@84,40,30
e076:0:ng B H:kneel@84,60,24 FX:mad2 FX:doom2
e076:1:r  B H:kneel@84,60,24 X:sparkle@84,74,8
e076:2:ok B H:jump@84,60,26
e076:2:ng B H:swim@84,78,30 FX:mad2
e077:0:ok BG X:door_open@84,70 X:coins@84,90,12 H:stand@40 X:sparkle@84,50,8
e077:0:ng B H:hurt@84,94,30 X:blood@84,98,16
e077:1:ok BG X:bones@84,90,14 H:listen@40 X:light@84,40,30
e077:1:ng B H:cower@40 X:text@84,40,8
e077:2:ok BG X:bones@84,92,20 H:fight@50 X:light@84,30,40
e077:2:ng B H:hurt@40 X:splat@60,60,8
e078:0:ok B H:carry@40 X:item@60,62,rope X:item@84,62,torch X:coins@60,94,6 noicons
e078:0:ng bg=cave H:fall@84,50,30 X:sparkle@84,60,30
e078:1:ok bg=flesh H:walk@84,96,30 X:stairs@84,99,3
e078:1:ng B H:hurt@84 X:blood@84,98,30 FX:red
e078:2:ok B H:walk@84,96,24 FX:quiet
e078:2:ng B H:hurt@84,90,30 FX:mad1
e079:0:r  B H:walk@60 X:stairs@120,98,5
e079:1:r  B H:sit@60 X:light@84,40,40
e079:2:r  B H:kneel@60 X:item@74,60,amulet noicons
''')

# ------------------------------------------------------------ tier 4
add('''
g075:2:ok B H:climb@84,52,22 X:stairs@84,99,3
g075:2:ng bg=chasm H:fall@84,60,30 X:splat@84,80,10
g075:3:ok BG P:dragon@0,10 H:arms_up@84,99,24 X:light@84,40,30
g075:3:ng B H:cower@84,99,26 X:text@84,40,12 FX:mad4
g075:4:ok B H:climb@24,80,26 FX:dark
g075:4:ng B H:hurt@30 X:flame@36,96,10 X:fire@30,99,3
e080:0:ok B H:slash@50+sword X:blood@100,96,20 X:stairs@120,99,3
e080:0:ng B H:cower@84 X:blood@84,98,24 FX:red
e080:1:ok B H:walk@84,96,30 FX:quiet
e080:1:ng B H:hurt@84 X:light@84,48,20 FX:red
e080:2:r  B H:walk@84,96,26 FX:mad1
e081:0:r  bg=flesh H:stand@84 X:rays@84,40,9
e081:1:ok B H:walk@84,96,30 FX:quiet
e081:1:ng B H:cower@84 FX:mad3
e081:2:ok bg=flesh H:slash@60+sword X:blood@84,96,24 X:splat@100,40,14
e081:2:ng B H:hurt@84 X:splat@84,50,14
e081:3:ok B H:stand@84 X:light@84,40,40
e081:3:ng B H:stand@84,96,38 FX:mad4 FX:quiet
e082:0:ok B H:reach@30 X:item@84,50,amulet X:rays@84,40,9 noicons
e082:0:ng bg=flesh X:blood@84,90,60 H:swim@84,80,30 FX:red
e082:1:ok B H:reach@30 X:light@84,50,40
e082:1:ng B H:hurt@30 FX:mad4
e082:2:r  B H:walk@150,96,26
e083:0:ok B H:jump@84,48,26
e083:0:ng B H:swim@84,70,30 X:hands@84,99,8
e083:1:ok B X:hands@84,70,6 H:down@84,60,30
e083:1:ng B X:hands@84,99,12 H:hurt@84,70,30 X:splat@84,50,6
e083:2:ok B H:kneel@84,52,26 X:light@84,60,30
e083:2:ng B X:hands@84,99,14 H:cower@84,60,28 FX:mad3
e084:0:ok BG X:light@84,30,60 X:rays@84,0,9 H:arms_up@84
e084:0:ng B H:slash@40+sword X:cracks@84,50,5
e084:1:ok BG X:rope@70,0,36 X:rope@98,0,36 H:point@50
e084:1:ng B H:kneel@40 FX:mad3
e084:2:r  BG X:light@84,40,60 X:sparkle@84,40,20 H:reach@50
e085:1:ok B H:walk@84,96,30 FX:quiet
e085:1:ng B H:walk@84,96,30 X:text@84,40,12 FX:mad2
e085:2:ok B H:run@84
e085:2:ng B H:down@84,97 X:mouth@120,40,12 X:text@60,40,6
e086:0:ok B H:jump@84,60,26 X:stairs@84,99,3
e086:0:ng B H:fall@84,50,30 FX:mad2
e086:1:ok B H:walk@84,96,26 FX:quiet
e086:1:ng B H:walk@50,96,22 H:walk@84,90,22 H:walk@118,84,22 FX:mad2
e086:2:ok bg=void H:fall@84,56,30 X:stairs@84,99,4
e086:2:ng bg=stairs H:fall@84,40,26
e087:0:ok B H:kneel@40 X:item@84,60,amulet noicons
e087:0:ng B H:cower@40 X:eyes@110,80,2 X:text@84,40,6
e087:1:ok B H:kneel@40 X:sparkle@84,70,8
e087:1:ng B H:kneel@40 FX:mad3 FX:quiet
e087:2:r  bg=flesh X:bones@84,96,4 H:pray@40 X:light@84,60,20
e088:0:ok BG H:slash@50+sword X:hooded@120,94,40 X:blood@120,98,14
e088:0:ng BG X:tentacles@100,99,4 H:hurt@84,80,34
e088:1:ok B H:pray@30 X:stairs@150,99,3
e088:1:ng B H:pray@30 X:eyes@84,40,6 FX:mad3
e088:2:ok BG X:bones@84,92,20 H:fight@40 X:sparkle@84,60,16
e088:2:ng B H:hurt@30 X:cracks@60,40,5
e089:0:ok B H:reach@30 X:light@40,50,26 X:sparkle@40,50,8
e089:0:ng B H:stand@30 FX:doom3
e089:1:ok bg=void H:fall@84,50,30 X:sparkle@84,50,30
e089:1:ng B H:climb@84,60,26 FX:mad1
e089:2:ok B H:drink@30 X:sparkle@40,50,10
e089:2:ng B H:hurt@30 X:blood@30,96,8
e090:0:ok B H:run@84,90,26
e090:0:ng B H:hurt@84,90,28 X:blood@84,96,20
e090:1:ok B H:walk@84,82,24 FX:quiet
e090:1:ng B H:cower@84,82,24 FX:mad2
e090:2:ok B X:zzz@100,40,3 H:walk@84,82,24
e090:2:ng B H:hurt@84,82,28 X:splat@84,60,10
e091:0:ok B H:walk@84,96,30 X:light@84,30,30
e091:0:ng B H:cower@84 X:text@84,40,14
e091:1:ok bg=void X:cracks@84,40,6 X:door_open@84,72 H:slash@50+sword
e091:1:ng B X:hands@84,99,10 H:hurt@84
e091:2:ok B H:walk@84,96,30 X:rays@84,0,5
e091:2:ng B H:stand@84 FX:mad4
e092:0:r  B H:reach@40 X:item@84,30,sword noicons
e092:1:ok BG X:light@84,20,60 X:sparkle@84,40,20 H:pray@50
e092:1:ng B H:stand@40 FX:mad2
e092:2:r  B H:listen@40 X:girl@140,92,14
e093:0:r  B H:reach@40 X:light@40,50,24 FX:wound2
e093:1:r  B H:reach@40 FX:mad2 FX:heal2
e093:2:r  B H:reach@40 X:item@70,60,amulet FX:doom2 noicons
e093:3:r  B H:reach@40 X:coins@60,92,6 X:sparkle@84,50,10
e094:0:ok B H:run@84
e094:0:ng B H:hurt@84 X:rays@84,30,9 FX:red
e094:1:ok B H:pray@84 X:light@84,30,40
e094:1:ng B H:cower@84 X:eyes@84,30,4 FX:mad4
e094:2:ok B H:arms_up@84 X:rays@84,30,9
e094:2:ng B H:cower@84 X:text@84,40,10 FX:mad3
e095:0:r  B X:girl@110,92,24 H:stand@60 X:light@84,40,50
e095:1:ok B H:sleep@84,96 X:light@84,50,30
e095:1:ng B H:sleep@84,96 FX:mad2 FX:dark
e095:2:ok B H:slash@60+sword X:cracks@110,50,5
e095:2:ng B H:hurt@60 X:tentacles@84,99,3
e096:0:ok B H:reach@60 X:light@44,36,24
e096:0:ng B H:reach@60 X:text@60,64,6 FX:mad2
e096:1:ok B H:sleep@124,64,30 X:light@124,60,30
e096:1:ng B H:sleep@124,64,30 X:hands@44,52,3 FX:mad2
e096:2:r  BG X:door_open@84,70 H:back@84,94,40
''')

# ------------------------------------------------------------ variations (keep every composition unique)
add('''
e016:2:r  bg=stairs H:walk@84,90,22 X:bones@84,96,6 FX:dark
e024:0:ng B H:cower@60 X:bats@84,40,10 FX:mad2
e026:2:r  B H:walk@150,94,26 X:text@84,52,3
e031:2:r  B H:back@130,96,34 X:sparkle@84,20,2
e033:2:ok B H:run@120,94,34 X:bones@60,94,6
e055:2:ok B H:run@50f
e085:2:ok B H:run@140,94,30 X:text@40,40,3
e094:0:ok B H:run@120 X:cracks@84,30,2
e031:1:ng B H:hurt@46 X:text@84,36,4 FX:mad1
e074:0:ok B H:drink@46 X:blood@46,96,6 X:light@46,50,26
e075:2:r  B H:back@84,98,40 X:text@84,30,6
e062:0:ok B H:run@40f X:tentacles@120,99,2
e081:1:ok B H:walk@84,96,30 X:eyes@84,50,4 FX:quiet
e085:1:ok B H:back@84,96,40 FX:quiet
''')
