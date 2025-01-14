# CommonFile

Object representing a file used in a request or response context 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_file_name** | **str** | The name of the file | 
**s_file_url** | **str** | The URL used to reach the File | [optional] 
**s_file_base64** | **bytearray** | The Base64 encoded binary content of the File | [optional] 
**e_file_source** | **str** | The source of the File | 

## Example

```python
from eZmaxApi.models.common_file import CommonFile

# TODO update the JSON string below
json = "{}"
# create an instance of CommonFile from a JSON string
common_file_instance = CommonFile.from_json(json)
# print the JSON string representation of the object
print(CommonFile.to_json())

# convert the object into a dict
common_file_dict = common_file_instance.to_dict()
# create an instance of CommonFile from a dict
common_file_from_dict = CommonFile.from_dict(common_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


