#Class experiments in GIMP Python
class Painting(object):
	"""Painting test class to deal 
	with all painting functions and data
	
	Attributes:
		name: string name for painting
		image: GIMP image
		height: image height
		width: image width
		file: string for file location
		saved: bool
	"""
	
	def __init__(self,imageIn,nameIn,):
		""" Returns a painting object whose name is nameIn
		and image is imageIn"""
		
		self.image = imageIn
		self.name = nameIn
		self.width = imageIn.width
		self.height = imageIn.height
		
	def setBrushSize(self,sizeIn):
		pdb.gimp_context_set_brush_size(sizeIn)



