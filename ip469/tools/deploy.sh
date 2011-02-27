
src_dir=$1
dest_dir=$2

cd $src_dir

cp __init__.py settings.py urls.py $dest_dir
cp -r static $dest_dir

mkdir $dest_dir/ip
cd ip
cp __init__.py urls.py views.py ip_convert.py models.py $dest_dir/ip
cd ..


