#DIP PROJECT : Face Recognition for Shopping marts
import modulex as mx
import time,random
from queue import Queue
import multiprocessing as mp

modules=['cmake','dlib','face_recognition','cv2']
try:
	#AUTO SATISFY DEPENDENCIES
	import face_recognition as fr
	import cv2
except:
	mx.auto_pip(modules)
	import face_recognition as fr
	import cv2




class Person:
	"""A default person Class, person has face and its encodings."""
	def __init__(self, name,faceImgFile):
		self.name=name
		self.faceID = fr.face_encodings(fr.load_image_file(faceImgFile))[0]
		self.faceImgFile=faceImgFile
	def is_present_in(self,scenaryimg):
		try:
			scenaryFaces=fr.face_encodings(scenaryimg)[0]
			return fr.compare_faces([self.faceID], scenaryFaces)[0]
		except Exception as e:
			# print(e)
			return False

def scan_person(personinstance):
	resultQueue=Queue(2)
	t=time.time()
	c=0
	video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	print("Started Scanning! please keep your big face infront of camera.\n")

	while True:
		ret, frame = video_capture.read()
		frame = cv2.resize(frame, (160, 120)) 
		cv2.imshow('video',frame)
		if not resultQueue.full():
			resultQueue.put(POOL.apply_async(Nikhil.is_present_in,(frame,)))
		if c%4==0:
			presence=resultQueue.get().get()

		if presence:
			print(personinstance.name,'has been identified')
			return presence

		if time.time()-t > 5:
			print('SCAN TIMEOUT!')
			print(personinstance.name,'Is not in the camera\'s view')
			return False

		cv2.waitKey(1)
		c+=1; time.sleep(1/10)

inventory={
	'apple':5,
	'mercedes_car':210*1000,
	'rolex_watch':399,
	'laptop':1200,
	'graphics_card':699,
	'chicken_biriyani':30,
	'television':1800,
	'private_jet':14*1000*1000,
	}

def do_shopping(Person,itemslist):
	total=0
	itemQty={}
	print(f'Initial_Balance: ${Person.bankBalance}')

	for item in itemslist:
		if itemQty.get(item,None):
			itemQty[item]+=1
		else:
			itemQty[item]=1
		Person.bankBalance-=inventory[item]
		total+=inventory[item]
	print('\n======> 🛒 SHOPPED ITEMS 🛒 <======')

	for item in sorted(itemQty.items()):
		print(f'{item[0]} = {item[1]} |',end=' ')
	print(f"\nShopping_bill: ${total:<8} | final_Balance: ${Person.bankBalance:<10}".upper())



if __name__ == '__main__':
	Nikhil=Person('NIKHIL','./faces/nikhilFaceID.jpg')
	Nikhil.bankBalance=1000*1000*1000 # Dollars
	POOL=mp.Pool(2)

	shoppedItems=random.choices(sorted(list(inventory.keys())) ,k=20)

	#authentication
	result=scan_person(Nikhil)

	if result:
		do_shopping(Nikhil,shoppedItems)
	else:
		print('We just did window shopping')
	