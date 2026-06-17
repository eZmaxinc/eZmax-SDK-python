# CustomEzmaxpartnerproductSubscribe

Request for POST /1/webhookdocumentation/subscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | [optional] 
**s_infrastructureenvironmenttype_description** | **str** | The environment type Description | [optional] 
**s_company_name1** | **str** | The Name of the Company in French | [optional] 
**s_company_name2** | **str** | The Name of the Company in English | [optional] 
**fki_systemconfigurationtype_id** | **int** | The unique ID of the Systemconfigurationtype | [optional] 
**s_systemconfigurationtype_description1** | **str** | The description of the Systemconfigurationtype in the language of the requester | [optional] 
**s_systemconfigurationtype_description2** | **str** | The description of the Systemconfigurationtype in the language of the requester | [optional] 
**fki_ezmaxpartner_id** | **int** | The unique ID of the Ezmaxpartner | [optional] 
**s_ezmaxpartner_name1** | **str** | The name of the Ezmaxpartner in french | [optional] 
**s_ezmaxpartner_name2** | **str** | The name of the Ezmaxpartner in english | [optional] 
**fki_ezmaxpartnerproduct_id** | **int** | The unique ID of the Ezmaxpartnerproduct | [optional] 
**s_ezmaxpartnerproduct_name1** | **str** | The name1 of the Ezmaxpartnerproduct | [optional] 
**s_ezmaxpartnerproduct_name2** | **str** | The name2 of the Ezmaxpartnerproduct | [optional] 
**fki_ezmaxpartnerproductstage_id** | **int** | The unique ID of the Ezmaxpartnerproductstage | [optional] 
**s_ezmaxpartnerproductstage_code** | **str** | The code of the sEzmaxpartnerproductstage | [optional] 
**s_user_login_name** | **str** | The login name of the User. | [optional] 
**s_user_first_name** | **str** | The first name of the user | [optional] 
**s_user_last_name** | **str** | The last name of the user | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | [optional] 
**obj_address** | [**AddressRequestCompound**](AddressRequestCompound.md) |  | [optional] 
**objphone** | [**PhoneRequestCompoundV2**](PhoneRequestCompoundV2.md) |  | [optional] 
**obj_email** | [**EmailRequestCompound**](EmailRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezmaxpartnerproduct_subscribe import CustomEzmaxpartnerproductSubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxpartnerproductSubscribe from a JSON string
custom_ezmaxpartnerproduct_subscribe_instance = CustomEzmaxpartnerproductSubscribe.from_json(json)
# print the JSON string representation of the object
print(CustomEzmaxpartnerproductSubscribe.to_json())

# convert the object into a dict
custom_ezmaxpartnerproduct_subscribe_dict = custom_ezmaxpartnerproduct_subscribe_instance.to_dict()
# create an instance of CustomEzmaxpartnerproductSubscribe from a dict
custom_ezmaxpartnerproduct_subscribe_from_dict = CustomEzmaxpartnerproductSubscribe.from_dict(custom_ezmaxpartnerproduct_subscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


