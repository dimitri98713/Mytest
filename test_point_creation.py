def test_point_creation():
	    p = point(22,7)
	
	def test_access_x_and_y():
	    assert 22 == getx(p)
	    assert 7 == gety(p)

Rouge

Lancez les tests: nosetests3 Constatez qu’ils échouent commitez !
Implémentation

def point(x,y):
	    return [x,y]
	
	def getx(p):
	    return p[0]
	
	def gety(p):
	    return p[1]

Quelques tests Utilisons des assertions simples pour le moment. def test_point_creation(): p = point(22,7) def test_access_x_and_y(): assert 22 == getx(p) assert 7 == gety(p)

