from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from database.models import Diagram

# Create your views here.

@login_required
def cd_editor(request):
    return render(request, 'cd_editor.html')


@login_required
def create_new_diagram(request):
    diagram = Diagram.our_create(name='', checked_out_by=request.user.username)
    session = request.session
    
    if 'diagram ids' not in session:
        session['diagram ids'] = [diagram.uid]
    else:
        if diagram.uid not in session['diagram ids']:
            session['diagram ids'].append(diagram.uid)
            session.save()

    diagrams = []
    
    #for diagram_id in session['diagram ids']:
        #diagram = get_model_by_uid(Diagram, uid=diagram_id)
        #diagrams.append(diagram)
        
    context={
        'diagram_id': diagram.uid,
        'diagrams' : diagrams,
    } 
                
    return render(request, 'create_diagram.html', context)