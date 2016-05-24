var c = db.resume_1_million.find({$or: [{"AdditionalInformation": {$ne:""}}, {"Skill": {$ne:""}}]});
while(c.hasNext()) {
  printjson(c.next());
}



// printjson(db.resume_1_million.find({$or: [{"AdditionalInformation": {$ne:""}}, {"Skill": {$ne:""}}]}).toArray())
// print(db.resume_1_million.find({$or: [{"AdditionalInformation": {$ne:""}}, {"Skill": {$ne:""}}]}).count())
