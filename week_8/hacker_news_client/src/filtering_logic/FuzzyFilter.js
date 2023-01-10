function getBigrams(string) {

    const s = string.toLowerCase()
    const v = s.split('');

    for (let i = 0; i < v.length; i++) {
        v[i] = s.slice(i, i + 2);
    }
    return v;
}
  
function StringSimilarity( string1, string2 ){

    if (string1.length > 0 && string2.length > 0) {

      const pairs1 = getBigrams(string1);
      const pairs2 = getBigrams(string2);
      const union = pairs1.length + pairs2.length;

      let hits = 0;

      for(var x=0; x<pairs1.length; x++){

        for(var y=0; y<pairs2.length; y++) {

            if( pairs1[x] === pairs2[y] ) {
                hits++;
            }
        }
    }

      if ( hits > 0 ) {
            return ((2.0 * hits) / union);
        }
    }
    return 0.0;
}


export default StringSimilarity;
