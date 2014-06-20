# WebROfs

WebROfs is a FUSE filesystem that allows read only mounting of a remote folder structure using plain HTTP. 

The files are simply copied to a web server and a manifest is generated and uploaded to the root of the structure that contains a description of all the files available. The client uses this to cache the entire folder structure avoiding uneccessary remote calls and to construct the correct URL to download the file when its read is requested.

Requires
--------

- Python >=3.2
- libfuse
- fusepy (included as fuse.py)

Using it
--------

1. Copy folder structure to your webserver, e.g. `/var/www/myfiles`
2. Generate manifest and save at root of structure `webrofs-manifest /var/www/myfiles > /var/www/myfiles/manifest`
3. On the client side mount the filesystem using `webrofs-fuse http://your-server/myfiles mount-point`

Why?
----

This filesystem can be mounted through proxies and firewalls. It can also be cached and load balanced to achieve high concurrent performance because it's just plain HTTP.
