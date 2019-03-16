#Series AP
void main() {
    int t;
    scanf("%d",&t);
    while(t--){
        int a,b,n;
        scanf("%d%d",&a,&b);
        scanf("%d",&n);
        int f,d,tn;
        f = a;
        d = (b-a);
        tn = f +((n-1)*d);
        printf("%d\n",tn);
    }
	
}