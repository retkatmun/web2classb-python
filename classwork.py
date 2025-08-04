blockfuse_labs = {
"web2_score":  {
     "john": 5,
     "mark": -5,
     "grace": 8,
     "abraham": 3
},

"web3_score": { 
     "lucky": 10,
     "aron": 3,
     "mark": 8
}
}

print(blockfuse_labs["web2_score"]["john"])
#blockfuse_labs.update({[web3_score][john]: 100})
blockfuse_labs["web2_score"].update({"john": 100})
blockfuse_labs["web2_score"]["john"] += 100
print(blockfuse_labs["web2_score"]["john"])
