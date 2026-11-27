# MultilingualDocumenttypeName

The name1 of the Documenttype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_documenttype_name1** | **str** | The name of the document type in French | [optional] 
**s_documenttype_name2** | **str** | The name of the document type in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_documenttype_name import MultilingualDocumenttypeName

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualDocumenttypeName from a JSON string
multilingual_documenttype_name_instance = MultilingualDocumenttypeName.from_json(json)
# print the JSON string representation of the object
print(MultilingualDocumenttypeName.to_json())

# convert the object into a dict
multilingual_documenttype_name_dict = multilingual_documenttype_name_instance.to_dict()
# create an instance of MultilingualDocumenttypeName from a dict
multilingual_documenttype_name_from_dict = MultilingualDocumenttypeName.from_dict(multilingual_documenttype_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


