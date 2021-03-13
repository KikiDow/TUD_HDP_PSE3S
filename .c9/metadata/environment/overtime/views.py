{"filter":false,"title":"views.py","tooltip":"/overtime/views.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":111,"column":71},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":112,"column":0},"end":{"row":112,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":112,"column":12},"end":{"row":114,"column":115},"action":"insert","lines":["if allowance_req_form.instance.claiming_breakfast_allowance == False and allowance_req_form.instance.claiming_dinner_allowance == False and allowance_req_form.instance.claiming_tea_allowance == False and allowance_req_form.instance.claiming_plain_clothes_allowance == False and allowance_req_form.instance.claiming_food_for_prisoner_expense == False:","                messages.error(request, \"You must select at least one allowance to make a valid allowance request.\")","                return render(request, \"submit_allowance_request.html\", {'allowance_req_form': allowance_req_form})"],"id":44}],[{"start":{"row":192,"column":85},"end":{"row":193,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":193,"column":0},"end":{"row":193,"column":20},"action":"insert","lines":["                    "]}],[{"start":{"row":193,"column":16},"end":{"row":193,"column":20},"action":"remove","lines":["    "],"id":46},{"start":{"row":193,"column":12},"end":{"row":193,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":193,"column":12},"end":{"row":208,"column":81},"action":"insert","lines":["else:","                allow_req_for_editing = edit_allow_req_form.save()","                total_claim_amount = 0.0","                if allow_req_for_editing.claiming_breakfast_allowance == True:","                    total_claim_amount += settings.BREAKFAST_ALLOWANCE","                if allow_req_for_editing.claiming_dinner_allowance == True:","                    total_claim_amount += settings.DINNER_ALLOWANCE","                if allow_req_for_editing.claiming_tea_allowance == True:","                    total_claim_amount += settings.TEA_ALLOWANCE","                if allow_req_for_editing.claiming_plain_clothes_allowance == True:","                    total_claim_amount += settings.PLAIN_CLOTHES_ALLOWANCE","                if allow_req_for_editing.claiming_food_for_prisoner_expense == True:","                    total_claim_amount += allow_req_for_editing.food_for_prisoner_amount                    ","                allow_req_for_editing.claim_total = total_claim_amount","                allow_req_for_editing.save()","                return redirect(view_allowance_request, allow_req_for_editing.pk)"],"id":47}],[{"start":{"row":169,"column":42},"end":{"row":170,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":170,"column":0},"end":{"row":170,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":170,"column":12},"end":{"row":172,"column":117},"action":"insert","lines":["if edit_allow_req_form.instance.claiming_breakfast_allowance == False and edit_allow_req_form.instance.claiming_dinner_allowance == False and edit_allow_req_form.instance.claiming_tea_allowance == False and edit_allow_req_form.instance.claiming_plain_clothes_allowance == False and edit_allow_req_form.instance.claiming_food_for_prisoner_expense == False:","                messages.error(request, \"You must select at least one allowance to make a valid allowance request.\")","                return render(request, \"submit_allowance_request.html\", {'edit_allow_req_form': edit_allow_req_form})"],"id":49}]]},"ace":{"folds":[],"scrolltop":2268,"scrollleft":0,"selection":{"start":{"row":172,"column":117},"end":{"row":172,"column":117},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":65,"state":"start","mode":"ace/mode/python"}},"timestamp":1615623883398,"hash":"b8a0380bb8c24e3e36e08c22654a443a895854dc"}