# https://docs.google.com/document/d/1VGDFYlpWuoqSuA41ZB9nPjzRNHUKrgew17ObczjIQbo/edit

from opentrons import labware, instruments

metadata = {
    'protocolName': 'Simple Dispenser',
    'author': '<chris.keith@gmail.com>'
}

micro_liters = 1

def run_custom_protocol(pipette_type: 'StringSelection...'='p300-Single',
                        source_labware_type: 'StringSelection...'='trough-12row',
                        destination_labware_type: 'StringSelection...'='96-flat'):
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

    source_container = labware.load(source_labware_type, '2')
    output_container = labware.load(destination_labware_type, '3')

    destination_wells = ['A1']
    source_well = source_container.wells('A1')

    pipette.distribute(
        micro_liters,
        source_well,
        output_container.wells(destination_wells),
        new_tip='once')

run_custom_protocol(**{'pipette_type': 'p300-Single',
                        'source_labware_type': 'trough-12row',
                        'destination_labware_type': '96-flat'})
