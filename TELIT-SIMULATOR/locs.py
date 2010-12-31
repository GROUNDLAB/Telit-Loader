#AVR SOURCE FILES FOR GSM,SERIAL FUNCTIONALITY###########################
# 	                                                   		#
#                    Copyright (C) 2010  Justin Downs of GRounND LAB	#
#                    www.GroundLab.cc  			1%      	#
#                     							#
#					Code based off:			#
#		      			Josh Levinger  			#
#			http://jlev.media.mit.edu/Projects/GeoTracker 	#
#					Further modified by:		#
#					Lucas Vickars	                #
# This program is free software: you can redistribute it and/or modify 	#
# it under the terms of the GNU General Public License as published by 	#
# the Free Software Foundation, either version 3 of the License, or    	#
# at your option) any later version.                                   	#
#                                                                      	#
# This program is distributed in the hope that it will be useful,      	#
# but WITHOUT ANY WARRANTY; without even the implied warranty of       	#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        	#
# GNU General Public License for more details.                         	#
#                                                                      	#
# You should have received a copy of the GNU General Public License    	#
# with this program.  If not, see <http://www.gnu.org/licenses/>.      	# 
#########################################################################


print "loading locations"

locs = (
('81 Highland Ave, Somerville, MA 02143 (Albert F. Argenziano School at Lincoln Park)', (42, 23, 12), (-72, 54, 8)),
('100 Putnam Ave, Cambridge, MA 02139 (Amigos School)', (42, 22, 2), (-72, 53, 11)),
('850 Cambridge St, Cambridge, MA 02141 (King Open)', (42, 22, 21), (-72, 54, 32)),
('197 Vassal Ln, Cambridge, MA 02138 (John M Tobin)', (42, 23, 2), (-72, 51, 36)),
('89 Elm St, Cambridge, MA 02139 (Cambridgeport)', (42, 22, 9), (-72, 54, 9)),
('40 Granite St, Cambridge, MA 02139 (Morse)', (42, 21, 21), (-72, 53, 18)),
('70 Rindge Ave, Cambridge, MA 02140 (Peabody)', (42, 23, 34), (-72, 52, 19)),
('28 Sacramento St, Cambridge, MA 02138 (Maria L. Baldwin)', (42, 22, 57), (-72, 52, 59)),
('110 Cushing St, Cambridge, MA 02138 (Haggerty)', (42, 22, 40), (-72, 50, 52)),
('44 Linnaean St, Cambridge, MA 02138 (Graham and Parks)', (42, 23, 0), (-72, 52, 34)),
('5 Cadbury Rd, Cambridge, MA 02140 (Cambridge Friends School)', (42, 23, 16), (-72, 52, 12)),
('1803 Massachusetts Ave, Cambridge, MA 02140 (Agassiz Preschool Inc)', (42, 23, 13), (-72, 52, 51)),
('45 Matignon Rd, Cambridge, MA 02140 (International School of Boston)', (42, 24, 7), (-72, 52, 2)),
('25 Francis Ave, Cambridge, MA 02138 (Oxford Street Day Care Cooperative)', (42, 22, 45), (-72, 53, 16)),
('20 Sacramento St, Cambridge, MA 02138 (Agassiz Community School-Child Care Program)', (42, 22, 57), (-72, 52, 56)),
('725 Concord Ave, Cambridge, MA 02138 (KinderCare Learning Centers)', (42, 23, 26), (-72, 50, 52)),
('24a Farwell Place, Cambridge, MA 02138 (Garden Nursery School)', (42, 22, 30), (-72, 52, 45)),
('80 Trowbridge St, Cambridge, MA 02138 (Cambridge Ellis School)', (42, 22, 31), (-72, 53, 24)),
('40 Blakeslee St, Cambridge, MA 02138 (Spring Hill Montessori School Inc)', (42, 22, 52), (-72, 51, 54)),
('40 Reservoir St # A, Cambridge, MA 02138 (Parent', (42, 22, 47), (-72, 51, 52)),
('343 Fresh Pond Pkwy, Cambridge, MA 02138 (Fresh Pond Recreation Area)', (42, 23, 22), (-72, 51, 30)),
('Munroe Street, Somerville, MA 02143 (Prospect Hill Park)', (42, 22, 52), (-72, 54, 26)),
('290 Washington St, Somerville, MA 02143 (Lincoln Park Community)', (42, 22, 43), (-72, 53, 57)),
('99 Sherman St, Cambridge, MA 02140 (Danehy Park)', (42, 23, 19), (-72, 52, 3)),
('Garden Street, Cambridge, MA 02138 (Cambridge Common)', (42, 22, 37), (-72, 52, 45)),
('165 Tremont St, Boston, MA 02111 (Boston Common)', (42, 21, 14), (-72, 56, 11)),
('607 Boylston St, Boston, MA 02116 (Copley Square)', (42, 21, 0), (-72, 55, 21)),
('9 Arlington St, Boston, MA 02116 (The Public Garden)', (42, 21, 16), (-72, 55, 46)),
('125 Arborway, Jamaica Plain, MA 02130 (Arnold Arboretum)', (42, 18, 27), (-72, 52, 48)),
('261 Riverside Avenue, Medford, Massachusetts (Mystic River Reservation)', (42, 24, 48), (-72, 54, 8)),
('147 Hampshire St, Cambridge, MA 02139 (Cambridge Parks Maintenance)', (42, 22, 16), (-72, 54, 9)),
('51 Inman St, Cambridge, MA 02139 (Cambridge Recreation Division)', (42, 22, 10), (-72, 53, 48)),
('Munroe Street, Somerville, MA 02143 (Prospect Hill Park)', (42, 22, 52), (-72, 54, 26)),
('290 Washington St, Somerville, MA 02143 (Lincoln Park Community)', (42, 22, 43), (-72, 53, 57)),
('74 Magazine St, Cambridge, MA 02139 (Dana Park)', (42, 21, 41), (-72, 53, 30)),
('Garden Street, Cambridge, MA 02138 (Cambridge Common)', (42, 22, 37), (-72, 52, 45)),
('1 Camp St, Cambridge, MA 02140 (Camp St Studio)', (42, 23, 54), (-72, 52, 11)),
('Cambridge, MA 02139 (Cronin Park)', (42, 21, 55), (-72, 53, 36)),
('22 Divinity Ave, Cambridge, MA 02138 (Arnold Arboretum)', (42, 22, 43), (-72, 53, 8)),
('22 Divinity Ave, Belmont, MA 02138 (Arnold Arboretum)', (42, 22, 38), (-72, 53, 10)),
)

print "locations loaded"