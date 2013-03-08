class Klasa(object):
	def __init__(self, meta):		
#		print "tu sam"
#		print meta.depth
        	self.depth = getattr(meta, 'depth', 0)
        	self.fields = getattr(meta, 'fields', ())
	        self.exclude = getattr(meta, 'exclude', ())

class Treca(object):
	class Meta:
		depth = 1
		fields = ("ivan", "pusic")
	def __init__(self):
		self.a = Klasa(self.Meta)
		print self.a.fields
		for key in self.a.fields:
			print key

if __name__ == "__main__":
	t = Treca()
