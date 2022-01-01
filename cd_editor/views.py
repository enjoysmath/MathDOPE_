from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from database.models import Diagram, get_model_by_name
from abstract_spacecraft.http_tools import get_url_text, render_error
from abstract_spacecraft.python_tools import full_qualname
import json

@login_required
def diagram_editor(request, diagram_name:str):
    try:        
        diagram = get_model_by_name(Diagram, diagram_name)
        json_str = json.dumps(diagram.quiver_format())       
        context = {
            'diagram_json': json_str,
            'diagram_name': diagram_name,
        }
        return render(request, 'diagram_editor.html', context)
    
    except Exception as e:
        return render_error(request, f'{full_qualname(e)}: {str(e)}')


#@login_required
#def create_new_diagram(request):
    #diagram = Diagram.our_create(name='', checked_out_by=request.user.username)
    #session = request.session
    
    #if 'diagram ids' not in session:
        #session['diagram ids'] = [diagram.uid]
    #else:
        #if diagram.uid not in session['diagram ids']:
            #session['diagram ids'].append(diagram.uid)
            #session.save()

    #diagrams = []
    
    ##for diagram_id in session['diagram ids']:
        ##diagram = get_model_by_uid(Diagram, uid=diagram_id)
        ##diagrams.append(diagram)
        
    #context={
        #'diagram_id': diagram.uid,
        #'diagrams' : diagrams,
    #} 
                
    #return render(request, 'create_diagram.html', context)