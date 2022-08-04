class india:
	elected = 'bhagwant maan'

	def minister(obj):
		print("CM: ", obj.elected)


india.minister = classmethod(india.minister)
india.minister()
