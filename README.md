# DDOS Botnet Based on Python

Created By Sabarisrinivas Venkatesan

## Zombie Mode Client

Client can be used for to launch the DDOS attacks on the target webservers based on the instructions from the C2 server. It connects to C2 Server and if the server is not available, the client terminates. If the C2 Server is availabe it tries to recieve a url from the C2 Server and launch attack on it. The client have no control over the target it attacks. 

## Flask based C2 Server

This is a flask based C2 Server that can be used to control multiple instances of client to coordinate attack on a same target.

## Disclaimer

This code is written only for educational and research purposes and is not inteded to be used for attacking any websites,servers or projects. 

## License

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise ) arising in any way out of the use of this software, even if advised of the possibility of such damage.