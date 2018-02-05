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

package serverantenna.simulations;

import inet.node.inet.INetworkNode;
import inet.node.inet.MulticastRouter;
import inet.node.inet.StandardHost;
import inet.node.internetcloud.InternetCloud;
import inet.node.wireless.AccessPoint;
import inet.networklayer.configurator.ipv4.IPv4NetworkConfigurator;
import inet.node.ethernet.Eth100M;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import inet.node.inet.WirelessHost;
import inet.node.wireless.AccessPoint;
import inet.node.xmipv6.CorrespondentNode6;
import inet.node.xmipv6.WirelessHost6;
import inet.physicallayer.ieee80211.packetlevel.Ieee80211ScalarRadioMedium;
import inet.visualizer.contract.IIntegratedVisualizer;
import ned.DatarateChannel;

//
// TODO auto-generated type
//
network Serverconnection
{
    parameters:
        int n;
        string hostType = default("WirelessHost");
        string mediumType = default("IdealRadioMedium");
        @display("bgb=7000,2000");

    types:
        channel C extends DatarateChannel
        {
            delay = 10ms;
            datarate = 5Mbps;
        }

    submodules:
        visualizer: <default("IntegratedCanvasVisualizer")> like IIntegratedVisualizer if hasVisualizer() {
            parameters:
                @display("p=64,14");
        }
        configurator: IPv4NetworkConfigurator {
            parameters:
                assignDisjunctSubnetAddresses = false;
                @display("p=64,58");
        }
        radioMedium: Ieee80211ScalarRadioMedium {
            parameters:
                @display("p=63,99");
        }
        LocalServer: StandardHost {
            @display("p=361.872,128.016");
        }
        host[n]: <hostType> like INetworkNode {
            @display("p=199.584,453.6");
        }
        router: Router {
            @display("p=361.872,201.6");
        }
        internetCloud: InternetCloud {
            @display("p=361.872,26.208");
        }
        GlobalServer: StandardHost {
            @display("p=663.26404,26.208");
        }
        accessPoint1: AccessPoint {
            @display("p=1500,400");
        }
        accessPoint2: AccessPoint {
            @display("p=2500,400");
        }
        accessPoint3: AccessPoint {
            @display("p=3500,400");
        }
        accessPoint: AccessPoint {
            @display("p=500,400");
        }
        accessPoint4: AccessPoint {
            @display("p=4500,400");
        }
    connections:
        GlobalServer.pppg++ <--> C <--> internetCloud.pppg++;
        LocalServer.pppg++ <--> C <--> internetCloud.pppg++;
        LocalServer.ethg++ <--> Eth100M <--> router.ethg++;
        router.ethg++ <--> Eth100M <--> accessPoint1.ethg++;
        router.ethg++ <--> Eth100M <--> accessPoint2.ethg++;
        router.ethg++ <--> Eth100M <--> accessPoint3.ethg++;
        router.ethg++ <--> Eth100M <--> accessPoint.ethg++;
        router.ethg++ <--> Eth100M <--> accessPoint4.ethg++;
}
