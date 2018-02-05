//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package vsnetwork.simulations;

import inet.applications.tcpapp.TCPEchoApp;
import inet.node.inet.StandardHost;
import inet.node.internetcloud.InternetCloud;
import inet.node.wireless.AccessPoint;
import inet.physicallayer.base.packetlevel.AntennaBase;


//
// TODO auto-generated type
//
network Antenna
{
    @display("bgb=769,405");
    submodules:
        accessPoint: AccessPoint {
            @display("p=466,241");
        }
        internetCloud: InternetCloud {
            @display("p=87,67;is=vl");
        }
        standardHost: StandardHost {
            @display("p=266,142");
        }
    connections:
}
