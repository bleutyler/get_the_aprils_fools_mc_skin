########################################
#
# MINECRAFT APRIL FOOLS RESOURCE PACK COLLECTOR
#
#
#
#
########################################
import os
import logging

from shutil import copyfile, rmtree


def create_resource_pack(*args, **kwargs):
	'Given environment variables, create a resource pack from the April Fools resource pack given to MC users April 1, 2018'
	if True:
		for item in args:
			logging.info('arg:' + item)
		for (k,v) in kwargs.items():
			logging.info('k/v:' + k + '/' + v)
		
	if not 'resource_pack_name' in kwargs:
		kwargs['resource_pack_name'] = 'POWER_FIST'
	if not 'minecraft_root_folder' in kwargs:
		folders_to_test = [r"C:\Users\Monika\AppData\Roaming\.minecraft"]
		for location in folders_to_test:
			if os.path.exists(location):
				kwargs['minecraft_root_folder'] = location
				break
	if not 'source_index_file' in kwargs:
		kwargs['source_index_file'] = kwargs['minecraft_root_folder'] + '\\assets\\indexes\\1.12-af.json'

	# optional
	if not 'pack_image_file' in kwargs:
		kwargs['pack_image_file'] = 'c:\python\pack.png'

		
	# create folder in resource_packs file
	# create pack.mcmeta
	# put in the default pack image file

	resource_pack_root_folder = kwargs['minecraft_root_folder'] + '\\resourcepacks\\' + kwargs['resource_pack_name']
	if not os.path.exists(resource_pack_root_folder):
		os.mkdir(resource_pack_root_folder)
	else:
		rmtree(resource_pack_root_folder)
		os.mkdir(resource_pack_root_folder)
	make_pack_mcmeta_file(resource_pack_root_folder + r'\pack.mcmeta')
	copyfile(kwargs['pack_image_file'], resource_pack_root_folder + '\\pack.png')

	# from the index file, find all files, and create the matching file in the new resourcepacks folder
	
	
	#kwargs['destination_file']
	#kwargs['destination_file']

def make_pack_mcmeta_file(destination_mcmetafile):
	#format is affected by MC version.  2 = MC v1.11 to v1.12
	pack_file_contents = '''{	
   "pack": {
      "pack_format": 3,
      "description": "POWER_FIST"
   }
}'''
	with open(destination_mcmetafile, 'w', encoding='utf-8') as destination_file:
		destination_file.write(pack_file_contents)
	
def get_variables_from_environment():
	logging.basicConfig( level=logging.INFO )
	create_resource_pack(minecraft_root_folder=r"C:\Users\Monika\AppData\Roaming\.minecraft", source_index_file=r"C:\Users\Monika\AppData\Roaming\.minecraft\assets\indexes\1.12-af.json"	)
	
if __name__ == '__main__':
	get_variables_from_environment()