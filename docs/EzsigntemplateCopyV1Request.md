# EzsigntemplateCopyV1Request

Request for POST /1/object/ezsigntemplate/{pkiEzsigntemplateID}/copy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_fki_ezsignfoldertype_id** | **List[int]** |  | [optional] 
**b_copy_company** | **bool** | Whether we shall copy the Ezsigntemplate as a company Ezsigntemplate | [optional] 
**b_copy_user** | **bool** | Whether we shall copy the Ezsigntemplate as a user Ezsigntemplate | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplate_copy_v1_request import EzsigntemplateCopyV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCopyV1Request from a JSON string
ezsigntemplate_copy_v1_request_instance = EzsigntemplateCopyV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCopyV1Request.to_json())

# convert the object into a dict
ezsigntemplate_copy_v1_request_dict = ezsigntemplate_copy_v1_request_instance.to_dict()
# create an instance of EzsigntemplateCopyV1Request from a dict
ezsigntemplate_copy_v1_request_from_dict = EzsigntemplateCopyV1Request.from_dict(ezsigntemplate_copy_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


