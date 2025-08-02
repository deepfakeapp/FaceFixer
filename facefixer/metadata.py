from typing import Optional

METADATA =\
{
	'name': 'FaceFixer',
	'description': 'FaceFixer - Industry leading face manipulation platform',
	'version': '3.3.2',
	'license': 'OpenRAIL-AS',
	'author': 'DeepFakeApp',
	'url': 'https://github.com/deepfakeapp'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
