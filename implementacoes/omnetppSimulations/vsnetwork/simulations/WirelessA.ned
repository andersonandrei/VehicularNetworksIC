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

import inet.common.figures.DelegateSignalConfigurator;
import inet.networklayer.configurator.ipv4.IPv4NetworkConfigurator;
import inet.node.inet.INetworkNode;
import inet.node.inet.Router;
import inet.node.wireless.AccessPoint;
import inet.physicallayer.base.packetlevel.AntennaBase;
import inet.physicallayer.contract.packetlevel.IRadioMedium;
import inet.visualizer.contract.IIntegratedVisualizer;


network WirelessA
{
    parameters:
        int n;
        string hostType = default("WirelessHost");
        string serverType = default("StandardHost");
        string mediumType = default("IdealRadioMedium");

        @display("bgb=900,600;bgg=100,1,grey95");
        @figure[title](type=label; pos=0,-1; anchor=sw; color=darkblue);

        @figure[rcvdPkText](type=indicatorText; pos=350,20; anchor=w; font=,18; textFormat="packets received host0: %g"; initialValue=0);
        @statistic[rcvdPk](source=host[0].udpApp[0].rcvdPk; record=figure(count); targetFigure=rcvdPkText);

//        @figure[rcvdPkText2](type=indicatorText; pos=350,40; anchor=w; font=,18; textFormat="packets received host1: %g"; initialValue=0);
//        @statistic[rcvdPk2](source=host[1].udpApp[0].rcvdPk; record=figure(count); targetFigure=rcvdPkText2);

//        @figure[rcvdPkText3](type=indicatorText; pos=350,60; anchor=w; font=,18; textFormat="packets received host2: %g"; initialValue=0);
//        @statistic[rcvdPk3](source=host[2].udpApp[0].rcvdPk; record=figure(count); targetFigure=rcvdPkText3);

//        @figure[rcvdPkText4](type=indicatorText; pos=350,80; anchor=w; font=,18; textFormat="packets received host3: %g"; initialValue=0);
//        @statistic[rcvdPk4](source=host[3].udpApp[0].rcvdPk; record=figure(count); targetFigure=rcvdPkText4);

//        @figure[rcvdPkText5](type=indicatorText; pos=350,100; anchor=w; font=,18; textFormat="packets received host4: %g"; initialValue=0);
//        @statistic[rcvdPk5](source=host[4].udpApp[0].rcvdPk; record=figure(count); targetFigure=rcvdPkText5);

//       @figure[rcvdPkText6](type=indicatorText; pos=350,120; anchor=w; font=,18; textFormat="packets received host5: %g"; initialValue=0);
//        @statistic[rcvdPk6](source=host[5].udpApp[0].rcvdPk; record=figure(count); targetFigure=rcvdPkText6);


    submodules:
        visualizer: <default("IntegratedCanvasVisualizer")> like IIntegratedVisualizer if hasVisualizer() {
            @display("p=786.24005,75.6");
        }
        configurator: IPv4NetworkConfigurator {
            @display("p=786.24005,118.944");
        }
        radioMedium: <mediumType> like IRadioMedium {
            @display("p=785.232,168.336");
        }
        server: <hostType> like INetworkNode {
            @display("p=444.544,299.58398;i=device/server");
        }
        host[n]: <hostType> like INetworkNode {
            @display("p=444.544,298.376");
        }
    connections:
}
