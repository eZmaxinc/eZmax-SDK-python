# EzsigntemplateGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**s_ezsigntemplate_filenamepattern** | **str** | The filename pattern of the Ezsigntemplate | [optional] 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**b_ezsigntemplate_editallowed** | **bool** | Whether the Ezsigntemplate if allowed to edit or not | 
**e_ezsigntemplate_type** | [**FieldEEzsigntemplateType**](FieldEEzsigntemplateType.md) |  | [optional] 
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponse**](EzsigntemplatedocumentResponse.md) |  | [optional] 
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerResponseCompound]**](EzsigntemplatesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_object_v1_response_m_payload import EzsigntemplateGetObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetObjectV1ResponseMPayload from a JSON string
ezsigntemplate_get_object_v1_response_m_payload_instance = EzsigntemplateGetObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateGetObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplate_get_object_v1_response_m_payload_dict = ezsigntemplate_get_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplateGetObjectV1ResponseMPayload from a dict
ezsigntemplate_get_object_v1_response_m_payload_form_dict = ezsigntemplate_get_object_v1_response_m_payload.from_dict(ezsigntemplate_get_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


