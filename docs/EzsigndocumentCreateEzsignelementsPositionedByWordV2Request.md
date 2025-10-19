# EzsigndocumentCreateEzsignelementsPositionedByWordV2Request

Request for POST /2/object/ezsigndocument/{pkiEzsigndocumentID}/createEzsignelementsPositionedByWord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignformfieldgroup** | [**List[CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest]**](CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest.md) |  | 
**a_obj_ezsignsignature** | [**List[CustomEzsignsignatureCreateEzsignelementsPositionedByWordRequest]**](CustomEzsignsignatureCreateEzsignelementsPositionedByWordRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v2_request import EzsigndocumentCreateEzsignelementsPositionedByWordV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV2Request from a JSON string
ezsigndocument_create_ezsignelements_positioned_by_word_v2_request_instance = EzsigndocumentCreateEzsignelementsPositionedByWordV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateEzsignelementsPositionedByWordV2Request.to_json())

# convert the object into a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v2_request_dict = ezsigndocument_create_ezsignelements_positioned_by_word_v2_request_instance.to_dict()
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV2Request from a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v2_request_from_dict = EzsigndocumentCreateEzsignelementsPositionedByWordV2Request.from_dict(ezsigndocument_create_ezsignelements_positioned_by_word_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


