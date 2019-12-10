# https://docs.google.com/document/d/1VGDFYlpWuoqSuA41ZB9nPjzRNHUKrgew17ObczjIQbo/edit

from opentrons import labware, instruments

metadata = {
    'protocolName': 'Simple Dispenser',
    'author': '<chris.keith@gmail.com>'
}

def run_custom_protocol(pipette_type: 'StringSelection...'='p300-Single',
                        source_labware_type: 'StringSelection...'='trough-12row',
                        destination_labware_type: 'StringSelection...'='96-flat',
                        micro_liters: 'NumberSelection...'=1,
                        new_tip_type: 'StringSelection...'='once'):
    if pipette_type == 'p300-Single':
        tiprack = labware.load('tiprack-200ul', '1')
        pipette = instruments.P300_Single(
            mount='right',
            tip_racks=[tiprack])
    elif pipette_type == 'p50-Single':
        tiprack = labware.load('tiprack-200ul', '1')
        pipette = instruments.P50_Single(
            mount='right',
            tip_racks=[tiprack])
    elif pipette_type == 'p10-Single':
        tiprack = labware.load('tiprack-10ul', '1')
        pipette = instruments.P10_Single(
            mount='right',
            tip_racks=[tiprack])
    else:
        print('Unknown pipette type: ' + pipette_type)
        return

    source_container = labware.load(source_labware_type, '2')
    destination_container = labware.load(destination_labware_type, '3')

    source_wells = source_container.wells('A1')
    destination_wells = destination_container.wells('A1')

    pipette.distribute(
        micro_liters,
        source_wells,
        destination_wells,
        new_tip=new_tip_type)

run_custom_protocol(**{'pipette_type': 'p300-Single',
                        'source_labware_type': 'trough-12row',
                        'destination_labware_type': '96-flat',
                        'micro_liters': 1,
                        'new_tip_type' : 'once'})
