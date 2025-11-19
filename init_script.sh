echo "A script to create , activate and install requirments.txt"
echo"....."
virtualenv venu

echo "creation of virtual done...."
echo "Activation my env"

source venv/bin/activate

echo "....."
echo "Install requirments.txt"

pip install -r requirments.txt

sleep(2)
echo "Install Done"
echo "Creation activation and install"
