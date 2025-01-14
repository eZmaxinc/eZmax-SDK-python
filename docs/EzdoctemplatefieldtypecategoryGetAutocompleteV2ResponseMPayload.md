# EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezdoctemplatefieldtypecategory/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezdoctemplatefieldtypecategory** | [**List[EzdoctemplatefieldtypecategoryAutocompleteElementResponse]**](EzdoctemplatefieldtypecategoryAutocompleteElementResponse.md) | An array of Ezdoctemplatefieldtypecategory autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezdoctemplatefieldtypecategory_get_autocomplete_v2_response_m_payload import EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload from a JSON string
ezdoctemplatefieldtypecategory_get_autocomplete_v2_response_m_payload_instance = EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
ezdoctemplatefieldtypecategory_get_autocomplete_v2_response_m_payload_dict = ezdoctemplatefieldtypecategory_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload from a dict
ezdoctemplatefieldtypecategory_get_autocomplete_v2_response_m_payload_from_dict = EzdoctemplatefieldtypecategoryGetAutocompleteV2ResponseMPayload.from_dict(ezdoctemplatefieldtypecategory_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


