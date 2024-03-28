# EzsigndocumentCreateEzsignelementsPositionedByWordV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/createEzsignelementsPositionedByWord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignformfieldgroup** | [**List[CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest]**](CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest.md) |  | 
**a_obj_ezsignsignature** | [**List[CustomEzsignsignatureCreateEzsignelementsPositionedByWordRequest]**](CustomEzsignsignatureCreateEzsignelementsPositionedByWordRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v1_request import EzsigndocumentCreateEzsignelementsPositionedByWordV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV1Request from a JSON string
ezsigndocument_create_ezsignelements_positioned_by_word_v1_request_instance = EzsigndocumentCreateEzsignelementsPositionedByWordV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateEzsignelementsPositionedByWordV1Request.to_json())

# convert the object into a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v1_request_dict = ezsigndocument_create_ezsignelements_positioned_by_word_v1_request_instance.to_dict()
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV1Request from a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v1_request_form_dict = ezsigndocument_create_ezsignelements_positioned_by_word_v1_request.from_dict(ezsigndocument_create_ezsignelements_positioned_by_word_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


