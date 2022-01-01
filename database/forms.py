from django.forms import Form, TextInput

class CreateDiagramForm(Form):
    diagram_name = TextInput()
    