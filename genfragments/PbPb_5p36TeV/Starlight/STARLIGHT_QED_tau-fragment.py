import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/RunIII/5p36TeV/starlight/starlight_ditau_el8_amd64_gcc11_CMSSW_13_0_18_HeavyIon_tarball.tgz'),
    nEvents = cms.untracked.uint32(1),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/blob/master/bin/Starlight/production/PbPb_5p36TeV/starlight_ditau.in

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8PSweightsSettingsBlock,
        skip_hadronization = cms.vstring(
            'ProcessLevel:all = off',
            'Check:event = off'
        ),
        parameterSets = cms.vstring('pythia8CommonSettings','pythia8PSweightsSettings','skip_hadronization')
    ),
    comEnergy = cms.double(5362.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

ProductionFilterSequence = cms.Sequence(generator)
