window.onload = function() {
  // sequence
  getId('sequence').innerHTML = sequence.match(/.{1,50}/g).join('<br>');
  getId('earth-logo').appendChild(getId('earth-svg'));
  // taxonomy
  getId('taxonomy-gg').innerHTML = taxonomyGG;
  getId('taxonomy-rdp').innerHTML = taxonomyRDP;
  getId('species-1st-rdp').innerHTML = speciesA;
  getId('species-2nd-rdp').innerHTML = speciesB;
  getId('species-2nd-rdp').innerHTML = speciesC;
  // wikipedia
  getId('wikipedia').innerHTML = wikipedia;
  // prevalence
  getId('prevalence-percent').innerHTML = prevalencePercent;
  getId('prevalence-rank').innerHTML = prevalenceRank;
  // abundance
  getId('abundance-percent').innerHTML = abundancePercent;
  getId('abundance-rank').innerHTML = abundanceRank;
  // method & misc
  getId('num-otus').innerHTML = numOTUs;
  getId('trim-length').innerHTML = trimLength;
  getId('num-samples').innerHTML = numSamples;
  getId('rarefaction-depth').innerHTML = rarefactionDepth;
  // chart by sample type
  getId('point-chart').appendChild(getId('point-svg'));
  getId('point-svg').style.height = '300px';
  getId('pie-chart').appendChild(getId('pie-svg'));
  getId('pie-svg').style.height = '300px';
  // chart by environmental parameters
  getId('envparams-chart').appendChild(getId('envparams-svg'));
};

// alias for document.getElementById
function getId(id) {
  return document.getElementById(id);
}

// show / hide an inline element
function toggle(e) {
  if (e.style.display == 'none') {
    e.style.display = 'inline';
  } else {
    e.style.display = 'none';
  }
}

// switch between point and pie charts
function toggleSampleTypeChart() {
  var elements = ['lbl-point', 'btn-point', 'lbl-pie', 'btn-pie', 'point-chart', 'pie-chart'];
  for (var i=0; i<elements.length; i++) {
    toggle(getId(elements[i]));
  }
}
