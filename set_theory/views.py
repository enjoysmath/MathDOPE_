from django.shortcuts import render

from .models import *

# Create your views here.

def test_page(request):   
   #op = Node(atomic_latex=r'\cap ').save()
   #A = Node(atomic_latex='A').save()
   #B = Node(atomic_latex='B').save()
   #C = BinaryOpExpr().save()
   #C.operator.connect(op)
   #C.left.connect(A)
   #C.right.connect(B)
   #C.save()
   
   #A = Class(atomic_latex='A').save()
   #B = Class(atomic_latex='B').save()
   
   #P = A*B
   
   #print(P.latex())
   
   load_default_theory()
   
   
   return render(request, 'test_page.html')