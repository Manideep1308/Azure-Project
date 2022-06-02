

echo "logging to azure portal.."
az login

echo "creating resource group"
az group create --name $1 --location centralus

echo "deploying ARM template"
az deployment group create --resource-group $1 --template-file $2