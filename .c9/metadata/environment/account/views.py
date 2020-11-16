{"filter":false,"title":"views.py","tooltip":"/account/views.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["g"],"id":16}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":[" "],"id":17},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["o"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["u"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":[" "],"id":18},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["u"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["s"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["e"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["r"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["."],"id":19}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":20}],[{"start":{"row":20,"column":0},"end":{"row":44,"column":48},"action":"insert","lines":["def login_view(request):","\tuser = request.user","\t#if user.is_authenticated: ","\t#\treturn redirect(\"home_page\")","","\tif request.POST:","\t\tlogin_form = AccountAuthenticationForm(request.POST)","\t\tif login_form.is_valid():","\t\t\temail = request.POST['email']","\t\t\tpassword = request.POST['password']","\t\t\tuser = authenticate(email=email, password=password)","","\t\t\tif user:","\t\t\t\tlogin(request, user)","\t\t\t\tmessages.success(request, \"You have successfully logged in\")","\t\t\t\t#Functions to check leave allowance, ah submission and leave submissions placed here.","\t\t\t\treturn redirect(\"home_page\")","","\telse:","\t\tlogin_form = AccountAuthenticationForm()","","\targs = {'login_form': login_form}","","\t# print(form)","\treturn render(request, \"login_page.html\", args)"],"id":21}],[{"start":{"row":22,"column":1},"end":{"row":23,"column":31},"action":"remove","lines":["#if user.is_authenticated: ","\t#\treturn redirect(\"home_page\")"],"id":22},{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":21,"column":20},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":20,"column":24},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":6},"action":"insert","lines":["''"],"id":24}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["'"],"id":25}],[{"start":{"row":21,"column":7},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":4},"end":{"row":23,"column":0},"action":"insert","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"insert","lines":["'"]},{"start":{"row":23,"column":5},"end":{"row":23,"column":6},"action":"insert","lines":["'"]}],[{"start":{"row":23,"column":6},"end":{"row":23,"column":7},"action":"insert","lines":["'"],"id":27}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["V"],"id":28},{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["i"]},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["e"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["w"]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":[" "],"id":29},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["u"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["s"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["e"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":[" "],"id":30},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["t"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":[" "],"id":31},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["l"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["o"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["g"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["i"]},{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":[" "],"id":32},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["u"]},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["s"]},{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["e"]},{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":["r"]},{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["s"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["."]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"remove","lines":["\t"],"id":33},{"start":{"row":23,"column":7},"end":{"row":24,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":23,"column":7},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":23},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":35}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"remove","lines":["\t"],"id":36},{"start":{"row":24,"column":23},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":23},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":1},"end":{"row":26,"column":2},"action":"remove","lines":["\t"],"id":38},{"start":{"row":26,"column":0},"end":{"row":26,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "],"id":39}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":8},"action":"insert","lines":["    "],"id":40}],[{"start":{"row":27,"column":1},"end":{"row":27,"column":2},"action":"remove","lines":["\t"],"id":41},{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "],"id":42}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":8},"action":"insert","lines":["    "],"id":43}],[{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"remove","lines":["\t"],"id":44},{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":45}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":8},"action":"insert","lines":["    "],"id":46}],[{"start":{"row":28,"column":8},"end":{"row":28,"column":12},"action":"insert","lines":["    "],"id":47}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"remove","lines":["\t"],"id":48},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":49}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"insert","lines":["    "],"id":50}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":12},"action":"insert","lines":["    "],"id":51}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":["\t"],"id":52},{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "],"id":53}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"insert","lines":["    "],"id":54}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":12},"action":"insert","lines":["    "],"id":55}],[{"start":{"row":32,"column":2},"end":{"row":32,"column":3},"action":"remove","lines":["\t"],"id":56},{"start":{"row":32,"column":1},"end":{"row":32,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":32,"column":0},"end":{"row":32,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "],"id":57}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"insert","lines":["    "],"id":58}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":12},"action":"insert","lines":["    "],"id":59}],[{"start":{"row":32,"column":12},"end":{"row":32,"column":16},"action":"insert","lines":["    "],"id":60}],[{"start":{"row":32,"column":12},"end":{"row":32,"column":16},"action":"remove","lines":["    "],"id":61}],[{"start":{"row":33,"column":3},"end":{"row":33,"column":4},"action":"remove","lines":["\t"],"id":62},{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":33,"column":1},"end":{"row":33,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "],"id":63}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"insert","lines":["    "],"id":64}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":12},"action":"insert","lines":["    "],"id":65}],[{"start":{"row":33,"column":12},"end":{"row":33,"column":16},"action":"insert","lines":["    "],"id":66}],[{"start":{"row":34,"column":3},"end":{"row":34,"column":4},"action":"remove","lines":["\t"],"id":67},{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":34,"column":1},"end":{"row":34,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "],"id":68}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":8},"action":"insert","lines":["    "],"id":69}],[{"start":{"row":34,"column":8},"end":{"row":34,"column":12},"action":"insert","lines":["    "],"id":70}],[{"start":{"row":34,"column":12},"end":{"row":34,"column":16},"action":"insert","lines":["    "],"id":71}],[{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"remove","lines":["\t"],"id":72},{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "],"id":73}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"insert","lines":["    "],"id":74}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":12},"action":"insert","lines":["    "],"id":75}],[{"start":{"row":36,"column":12},"end":{"row":36,"column":16},"action":"insert","lines":["    "],"id":76}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":1},"action":"remove","lines":["\t"],"id":77}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "],"id":78}],[{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"remove","lines":["\t"],"id":79},{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "],"id":80}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":8},"action":"insert","lines":["    "],"id":81}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":1},"action":"remove","lines":["\t"],"id":82},{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":83}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "],"id":84}],[{"start":{"row":43,"column":1},"end":{"row":43,"column":14},"action":"remove","lines":["# print(form)"],"id":85},{"start":{"row":43,"column":0},"end":{"row":43,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"remove","lines":["",""]},{"start":{"row":41,"column":37},"end":{"row":42,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"remove","lines":["\t"],"id":86}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "],"id":87}],[{"start":{"row":42,"column":51},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "],"id":89}],[{"start":{"row":43,"column":0},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":90}],[{"start":{"row":44,"column":0},"end":{"row":48,"column":44},"action":"insert","lines":["@login_required()","def home_page(request):","    total_users = Account.objects.count()","    print(\"Number of Users: \" + str(total_users))","    return render(request, 'home_page.html')"],"id":91}],[{"start":{"row":46,"column":4},"end":{"row":47,"column":49},"action":"remove","lines":["total_users = Account.objects.count()","    print(\"Number of Users: \" + str(total_users))"],"id":92}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":6},"action":"insert","lines":["''"],"id":93}],[{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["'"],"id":94}],[{"start":{"row":46,"column":7},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":95},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["V"]}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["i"],"id":96},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["e"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["w"]}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":[" "],"id":97}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"remove","lines":[" "],"id":98},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"remove","lines":["w"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"remove","lines":["e"]},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"remove","lines":["i"]},{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"remove","lines":["V"]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["V"],"id":99},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["i"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["e"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["w"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":[" "],"id":100},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["r"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["e"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["n"]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["d"]},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":["e"]},{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"insert","lines":["r"]},{"start":{"row":47,"column":16},"end":{"row":47,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":17},"end":{"row":47,"column":18},"action":"insert","lines":[" "],"id":101},{"start":{"row":47,"column":18},"end":{"row":47,"column":19},"action":"insert","lines":["h"]},{"start":{"row":47,"column":19},"end":{"row":47,"column":20},"action":"insert","lines":["o"]},{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"insert","lines":["m"]},{"start":{"row":47,"column":21},"end":{"row":47,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"insert","lines":[" "],"id":102},{"start":{"row":47,"column":23},"end":{"row":47,"column":24},"action":"insert","lines":["p"]},{"start":{"row":47,"column":24},"end":{"row":47,"column":25},"action":"insert","lines":["a"]},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"insert","lines":["g"]},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"insert","lines":[" "],"id":103},{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"insert","lines":["t"]},{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"insert","lines":[" "],"id":104},{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"insert","lines":["u"]},{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"insert","lines":["s"]},{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"insert","lines":["e"]},{"start":{"row":47,"column":34},"end":{"row":47,"column":35},"action":"insert","lines":["r"]}],[{"start":{"row":47,"column":35},"end":{"row":47,"column":36},"action":"insert","lines":[" "],"id":105},{"start":{"row":47,"column":36},"end":{"row":47,"column":37},"action":"insert","lines":["a"]},{"start":{"row":47,"column":37},"end":{"row":47,"column":38},"action":"insert","lines":["f"]},{"start":{"row":47,"column":38},"end":{"row":47,"column":39},"action":"insert","lines":["t"]},{"start":{"row":47,"column":39},"end":{"row":47,"column":40},"action":"insert","lines":["e"]},{"start":{"row":47,"column":40},"end":{"row":47,"column":41},"action":"insert","lines":["r"]}],[{"start":{"row":47,"column":41},"end":{"row":47,"column":42},"action":"insert","lines":[" "],"id":106},{"start":{"row":47,"column":42},"end":{"row":47,"column":43},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":42},"end":{"row":47,"column":43},"action":"remove","lines":["o"],"id":107},{"start":{"row":47,"column":41},"end":{"row":47,"column":42},"action":"remove","lines":[" "]},{"start":{"row":47,"column":40},"end":{"row":47,"column":41},"action":"remove","lines":["r"]},{"start":{"row":47,"column":39},"end":{"row":47,"column":40},"action":"remove","lines":["e"]},{"start":{"row":47,"column":38},"end":{"row":47,"column":39},"action":"remove","lines":["t"]},{"start":{"row":47,"column":37},"end":{"row":47,"column":38},"action":"remove","lines":["f"]}],[{"start":{"row":47,"column":36},"end":{"row":47,"column":37},"action":"remove","lines":["a"],"id":108},{"start":{"row":47,"column":35},"end":{"row":47,"column":36},"action":"remove","lines":[" "]}],[{"start":{"row":47,"column":35},"end":{"row":47,"column":36},"action":"insert","lines":["."],"id":109}],[{"start":{"row":47,"column":36},"end":{"row":47,"column":41},"action":"insert","lines":["Views"],"id":110}],[{"start":{"row":47,"column":40},"end":{"row":47,"column":41},"action":"remove","lines":["s"],"id":111},{"start":{"row":47,"column":39},"end":{"row":47,"column":40},"action":"remove","lines":["w"]},{"start":{"row":47,"column":38},"end":{"row":47,"column":39},"action":"remove","lines":["e"]},{"start":{"row":47,"column":37},"end":{"row":47,"column":38},"action":"remove","lines":["i"]},{"start":{"row":47,"column":36},"end":{"row":47,"column":37},"action":"remove","lines":["V"]}],[{"start":{"row":47,"column":36},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":112},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["'"]},{"start":{"row":48,"column":5},"end":{"row":48,"column":6},"action":"insert","lines":["'"]},{"start":{"row":48,"column":6},"end":{"row":48,"column":7},"action":"insert","lines":["'"]}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"remove","lines":["    "],"id":113}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "],"id":114}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["#"],"id":115}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["#"],"id":116}]]},"ace":{"folds":[],"scrolltop":70,"scrollleft":0,"selection":{"start":{"row":7,"column":1},"end":{"row":7,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1605545390295,"hash":"11fd799f05659ba74ebc9907837ef8ab36bffeac"}