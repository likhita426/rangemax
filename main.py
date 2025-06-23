def query(tree,node,s,e,l,r):
    if l>e or r<s:
        return 0
    elif l<=s and r>=e:
        return tree[node]
    else:
        mid=(s+e)//2 
        left=query(tree,2*node+1,s,mid,l,r)
        right=query(tree,2*node+2,mid+1,e,l,r)
        return max(left,right)
def update(arr,tree,node,s,e,i,v):
    if s==e:
        arr[i]=v 
        tree[node]=v 
        return
    else:
        mid=(s+e)//2
        if i<=mid:
            update(arr,tree,2*node+1,s,mid,i,v)
        else:
            update(arr,tree,2*node+2,mid+1,e,i,v)
        tree[node]=max(tree[2*node+1],tree[2*node+2])    
        
            
def build(arr,tree,n,s,e):
    if s==e:
        tree[n]=arr[s]
        return
    else:
        mid=(s+e)//2
        build(arr,tree,2*n+1,s,mid)
        build(arr,tree,2*n+2,mid+1,e)
        tree[n]=max(tree[2*n+1],tree[2*n+2])
arr=[3,1,2,5,6]
tree=[0]*(4*len(arr))
build(arr,tree,0,0,len(arr)-1)
print(query(tree,0,0,len(arr)-1,2,5))
update(arr,tree,0,0,len(arr)-1,2,5)
print(tree)

