<div style="background-color: #c8ccce; height: 28px; position:relative"><h3 style="display: inline-block;
    top: -1px;
    left: -2px;
    box-shadow: 1px 1px 1px 1px #333;
    background-color: #4096EE;
    position: absolute;
    margin: 0;
    font-size: 12px !important;
    line-height: 28px;
    padding: 0px 16px;
    font-weight: normal;
text-transform:uppercase;
    color: #ffffff;">PuTTY</h3></div>
	<pre class="alt2 prettyprint linenums" dir="ltr" style="
		margin: 0px;
		padding: 6px;
		text-align: left;
		overflow: auto;
		white-space: pre-wrap;
		white-space: -moz-pre-wrap;
		white-space: -pre-wrap;
		white-space: -o-pre-wrap;
		word-wrap: break-word; 
word-break: break-all;
background-color: #333; color: #fff;">CFE> ATHE
Available commands:

ATSE                show the seed of password generator
ATEN                set BootExtension Debug Flag
ATCR                Clear console screen
ATSH                dump manufacturer related data in ROM
ATUR                xmodem upload router firmware to flash ROM
FWSELECT            Select partition to read/write image or show FW version
ATIR                Set ImageDefault to ROM-D partition
ATER                Erase ROM-D partition
ATBL                Print boot line and board parameter info
ATDU                Dump memory or registers.
ATBR                Reset to default Romfile
ATGO                boot router
ATSR                system reboot
ATMB                Use for multiboot.
ATHE                print help

For more information about a command, enter 'help command-name'
*** command status = 0
CFE> ATSH

FW       Version       : 
Bootbase Version       : 
Vendor Name            :
Product Model          : DSL-2492GNAU-B3BC
Serial Number          : 
WPA-PSK                : 
First MAC Address      : 
Last MAC Address       : 
MAC Address Quantity   : 
Default Country Code   : 
Boot Module Debug Flag : 
RootFS      Checksum   : 
ImageDefaultChecksum   : 
Main Feature Bits      : 
Other Feature Bits     :
                4d 53 60 0a 00 00 00 00-00 00 00 00 00 00 00 00
                00 00 00 00 00 00 00 00-00 00 00 00 00 00

*** command status = 0
CFE> ATSE DSL-2492GNAU-B3BC

000D4548B61F
OK
*** command status = 0
CFE> ATEN 1 5021EC20

OK
*** command status = 0
CFE>
</pre>
</div>
